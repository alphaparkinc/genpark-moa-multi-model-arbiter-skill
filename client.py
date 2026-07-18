from collections import Counter

class MoaMultiModelArbiterClient:
    def arbitrate(self, model_responses: dict) -> dict:
        if not model_responses:
            return {"consensus_answer": "", "confidence_score": 0.0}
        responses = list(model_responses.values())
        vote_count = Counter(responses)
        best_answer, votes = vote_count.most_common(1)[0]
        confidence = round(votes / len(responses), 2)
        return {"consensus_answer": best_answer, "confidence_score": confidence}
