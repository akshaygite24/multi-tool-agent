def run_app(agent_executor):
    print("Agent is ready Type 'exit' to quit.\n")

    while True:
        query = input("Ask: ")

        if query.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        try:
            response = agent_executor.invoke({
                "input": query
            })
            print(f"Answer {response["output"]}")
        except Exception as e:
            print(f"Error : {str(e)}")

