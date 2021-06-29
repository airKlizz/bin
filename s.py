from elg import FlaskService
from elg.model import ClassificationResponse, ClassesResponse

class CredibilityScoreService(FlaskService):
    def convert_outputs(self, content: str) -> ClassificationResponse:
        score: float = 0.85
        return ClassificationResponse(classes=[ClassesResponse(score=score)])
    def process_text(self, content):
        return self.convert_outputs(content.content)



flask_service = CredibilityScoreService("")
app = flask_service.app