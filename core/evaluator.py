class Evaluator:

    def evaluate(self, state, history):

        score = 0

        if state["completed"]:
            score += 100

        score -= len(history)

        return {
            "success": state["completed"],
            "score": score,
            "steps": len(history)
        }
