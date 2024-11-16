from memoripy import MemoryManager, JSONStorage
import time

def main():
    # Initialize with Ollama (no API key needed)
    memory_manager = MemoryManager(
        api_key="not-needed",  # Not needed for Ollama
        chat_model="ollama",
        chat_model_name="phi3",  # Using phi3 which is fast and small
        embedding_model="ollama",
        embedding_model_name="phi3",  # Using same model for embeddings
        storage=JSONStorage("memory_demo_history.json")
    )

    # Add an initial interaction
    prompt = "What is the capital of France?"
    response = memory_manager.generate_response(prompt, [], [])
    embedding = memory_manager.get_embedding(prompt + " " + response)
    concepts = memory_manager.extract_concepts(prompt + " " + response)
    memory_manager.memory_store.add_interaction({
        "id": "1",
        "prompt": prompt,
        "output": response,
        "embedding": embedding,
        "concepts": concepts
    })

    # Simulate accessing this memory multiple times
    print("\nSimulating multiple accesses to move memory to long-term storage...")
    for i in range(12):  # More than 10 times to trigger long-term memory transfer
        query = "Tell me about France's capital"
        relevant = memory_manager.retrieve_relevant_interactions(query)
        print(f"Access {i+1}: Found {len(relevant)} relevant interactions")
        time.sleep(1)  # Small delay to see the process

    # Check memory status
    print("\nMemory Status:")
    print(f"Short-term memories: {len(memory_manager.memory_store.short_term_memory)}")
    print(f"Long-term memories: {len(memory_manager.memory_store.long_term_memory)}")
    
    # Save the memory state
    memory_manager.save_memory_to_history()

if __name__ == "__main__":
    main()
