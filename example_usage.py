from client import MoaMultiModelArbiterClient
client = MoaMultiModelArbiterClient()
result = client.arbitrate({
    "gpt5": "Paris",
    "claude": "Paris",
    "gemini": "London",
    "grok": "Paris"
})
print(f"Consensus: {result['consensus_answer']} (confidence: {result['confidence_score']})")
