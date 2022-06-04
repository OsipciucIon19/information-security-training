import math
import pdfkit
from CourseIterator.Progress import Progress

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


class Handler:
    def __init__(self):
        self.nextHandler = None

    def handle(self, request):
        self.nextHandler.handle(request)


class PDFHandler(Handler):
    def handle(self, request):
        self.output_report(request.courses)

    def output_report(self, courses):
        progress = Progress(courses)
        iterator = progress.iterator()

        string = '<html>'
        string += '<head>'
        string += '<title>Progress Report</title>'
        string += '</head>'
        string += '<body>'
        string += '<div>'
        string += '<h2>Your current training progress:</h2>'
        summa = 0
        while iterator.has_next():
            course = iterator.next()
            summa += int(course[1])
            string += f'<p>{course[0]} --> {course[1]} %</p>'
        string += '<hr/>'
        string += f'<p>Overall progress --> {math.trunc(summa / len(courses))} %</p>'
        string += '</div>'
        string += '</body>'
        string += '</html>'

        pdfkit.from_string(string, 'training-report.pdf', configuration=config)


class GUIHandler(Handler):
    def handle(self, request):
        if request.format_ == 'gui':
            return self.output_report(request.courses)
        else:
            super(GUIHandler, self).handle(request)

    def output_report(self, courses):
        progress = Progress(courses)
        iterator = progress.iterator()

        summa = 0
        while iterator.has_next():
            course = iterator.next()
            summa += int(course[1])

        return math.trunc(summa / len(courses))
