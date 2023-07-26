import termcolor


class MyPrint:
    '''
    A class to print colored text in terminal using termcolor package 
    '''
    def __init__(self, success_color='green', warning_color='yellow', error_color='red', default_color='grey'):
        self.success_color = success_color
        self.warning_color = warning_color
        self.error_color = error_color
        self.default_color = default_color

    def success(self, text, end='\n'):
        '''
        Print text in green color with bold and reverse attributes
        '''
        self._print(text, self.success_color, end)

    def warning(self, text, end='\n'):
        '''
        Print text in yellow color with bold and reverse attributes
        '''
        self._print(text, self.warning_color, end)

    def error(self, text, end='\n'):
        '''
        Print text in red color with bold and reverse attributes
        '''
        self._print(text, self.error_color, end)

    def gray(self, text, end='\n'):
        '''
        Print text in gray color with bold and reverse attributes
        '''
        self._print(text, self.default_color, end)

    def _print(self, text, color, end):
        '''
        Print text in a given color with bold and reverse attributes
        '''
        print(termcolor.colored(text, color, attrs=["bold", "reverse"]), end=end)