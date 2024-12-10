from PyQt6.QtWidgets import *
from output import *
from liveLoad import *
from gui import *
'''
Adam Becker
1620
12/09/2024
'''


class Logic(QMainWindow,Ui_SimpleSpanLoadProgram):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.solution = [] #creates an empty list for the beam results
        self.load_name = ""  #intialize the load name
        self.length = 0     #initialize the span length
        self.button_run.clicked.connect(lambda : self.execute())
        self.button_create_csv.clicked.connect(lambda: self.save_to_csv(self.solution))

    def execute(self):
        '''
        This definition determines what load was selected from the radio buttons
        and what length the user wants the analysis done on.  It also checks the
        user input for span length to ensure valid entry.
        :return:
        '''
        span_length = self.input_span_length.text().strip()
        self.length, correct = self.check_span_length(span_length) #checks if length input is good

        if correct == 'y':
            '''This determines which radio button is pushed'''
            if self.radio_E5.isChecked():
                axle_loads = e5_ld
                axle_spacing = e10_axleLoc
                self.load_name = "E5"
            elif self.radio_E10.isChecked():
                axle_loads = e10_ld
                axle_spacing = e10_axleLoc
                self.load_name = "E10"
            elif self.radio_E40.isChecked():
                axle_loads = e40_ld
                axle_spacing = e10_axleLoc
                self.load_name = "E40"
            elif self.radio_E80.isChecked():
                axle_loads = e80_ld
                axle_spacing = e10_axleLoc
                self.load_name = "E80"
            elif self.radio_268A.isChecked():
                axle_loads = UP268a_ld
                axle_spacing = UP268a_axleLoc
                self.load_name = "268A"
            elif self.radio_286A.isChecked():
                axle_loads = UP286a_ld
                axle_spacing = UP286a_axleLoc
                self.load_name = "286A"
            elif self.radio_315A.isChecked():
                axle_loads = UP315a_ld
                axle_spacing = UP315a_axleLoc
                self.load_name = "315A"
            else:
                axle_loads = alt_load
                axle_spacing = alt_loc
                self.load_name = "Alternate Load"

            #The following call puts the load results into the self.solution list.
            self.solution = span_results(axle_loads, axle_spacing, self.length)

            #The following call prints the load results to the python window.
            self.print_output(self.solution)
            for t in range(len(self.solution)):
                print(f'D = {self.solution[t][0]:.1f}ft, Max Shear = {self.solution[t][1]:,.2f} k, Max Moment = {self.solution[t][2]:,.2f} k*ft')

            #write_to_csv(solution)

    def print_output(self,solution):
        '''
        This definition prints the results of the load analysis into a text box in the gui.
        :param solution: A list of lists with the results from the load analysis.
        :return:
        '''
        self.textbox_results.clear()

        self.textbox_results.append(f'Results for {self.load_name} load and {self.length:.2f} ft long span.')
        self.textbox_results.append('----------------------------------------------------------')

        header = "    Distance (ft),                Shear (kips),                Moment (kip*ft)"
        self.textbox_results.append(header)

        v = 0
        m = 0
        #the following loop prints each item in the results list as well as keeps
        #track of the max shear and moment in the list to report at the end.
        for t in range(len(solution)):
            distance, shear, moment = solution[t]
            if shear > v:
                v = shear
            if moment > m:
                m = moment
            result = f'Location = {distance:.2f}ft,   Max Shear = {shear:,.2f} k,   Max Moment = {moment:,.2f} k*ft'
            self.textbox_results.append(result)
        self.textbox_results.append('')
        self.textbox_results.append(f'Max Shear = {v:,.2f} kips')
        self.textbox_results.append(f'Max Moment = {m:,.2f} kip*ft')



    def save_to_csv(self,solution):
        '''
        This definition executes every time the save to csv file button is pushed.
        It puts the span results into a csv file for easy copying into a design file.
        :param solution: A full list of the load results for the span.
        :return:
        '''
        write_to_csv(solution)

    def check_span_length(self, span_length):
        '''
        This definition checks the input for span length to ensure it can
        be turned into an integer and is between 1 and 450.
        :param span_length:
        :return:
        '''
        try:
            length = float(span_length)
            if 1 <= length <= 450:
                return length, 'y'
            else:
                self.label.setText("Please re enter a number between 1 and 450.")
                self.input_span_length.clear()
                self.input_span_length.setFocus()
                return -1, 'n'
        except ValueError:
            self.label.setText('Please re enter a number between 1 and 450.')
            self.input_span_length.clear()
            self.input_span_length.setFocus()
            return -1,'n'