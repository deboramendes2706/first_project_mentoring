from pydantic import BaseModel


class InputPredict(BaseModel):
    type_school: str
    school_accreditation: str
    gender: str
    interest: str
    residence: str
    parent_salary: int
    average_grades: float
    parent_was_in_college: bool


class ResponsePredict(BaseModel):
    will_go_to_college: bool
    will_go_to_college_text: str
