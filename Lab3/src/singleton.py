class Logger:
    _instance = None  # Private class variable to hold the single instance

    # can also use __init__ below to implement the logic if delete:
    # line 17: cls._instance.init_Logger() and line 22-23 for def init_Logger(self)
    # def __init__(self):
    #     if not hasattr(self, 'messages'):
    #         self.messages = []
    def __init__(self):
        pass

    def add_message(self, message):
        self.messages.append(message)
    
    # cls: the class of which an instance was requested
    def __new__(cls):
        if cls._instance is None:
            print('Logger created exactly once')
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.init_Logger()
        else:
            print('logger already created')
        return cls._instance
    
    # This may be the *instance* member function required, but I create an object in __new__ instead of here
    def init_Logger(self):
        self.messages = []


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")
        # print(logger.messages) # for debugging


if __name__ == "__main__":
    main()
