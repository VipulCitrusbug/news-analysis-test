from fastapi.responses import JSONResponse
from fastapi import status


class CustomResponse:
    def __init__(self, status_code=status.HTTP_200_OK, data=None, message=""):
        self.status_code = status_code
        self.data = data
        self.message = message

    def response(self):
        self.data_dict = {"data": self.data, "message": self.message}
        return JSONResponse(status_code=self.status_code, content=self.data_dict)
