from abc import ABC, abstractmethod


class WebApplicationTemplateFramework(ABC):
    def handle_request(self, request):
        self.authenticate(request)
        self.route_request(request)
        self.execute_bussiness_logic(request)
        self.render_response(request)

    def authenticate(self, request):
        print(f"Authenticating the {request}")

    def route_request(self, request):
        print(f"Routing the {request} to proper handler")

    @abstractmethod
    def execute_bussiness_logic(self, request):
        pass

    def render_response(self, request):
        print(f"Rendering the {request} response through {self.__class__.__name__}")


class DjangoFramework(WebApplicationTemplateFramework):
    def execute_bussiness_logic(self, request):
        print(
            f"Executing the bussiness logic for {request} through {self.__class__.__name__}"
        )


class FlaskFramework(WebApplicationTemplateFramework):
    def execute_bussiness_logic(self, request):
        print(
            f"Executing the bussiness logic for {request} through {self.__class__.__name__}"
        )


if __name__ == "__main__":
    django = DjangoFramework()
    flask = FlaskFramework()

    django.handle_request("GET:/users")
    print("\n-\n" * 2)
    flask.handle_request("POST:/submit")
