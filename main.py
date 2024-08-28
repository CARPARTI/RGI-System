from datetime import datetime
class Application:
    def __init__(self):
        self.__user = None
        self.latest_notice_amm = 0.0
        self.eligible()  # Automatically run the eligibility check upon initialization


    def eligible(self):
        print("Is the individual currently entitled to Rent-Geared-to-Income (RGI) and having their eligibility reviewed?  \n Yes or No")
        answer = input()
        if answer.lower() in ["yes", "y"]:
            print("Application is relevant")
            self.print_type_of_household()


        else:
            print("Please conduct more research that may be more relevant to the individuals situation")

    def print_type_of_household(self):
        type = input("Choose a Number that best represents your case "
                     "\n 1: Household with at least one benefit unit "
                     "\n 2: Household with at least one family unit that is NOT, and no part of which is a benefit unit "
                     "\n 3: Household has at least one family unit a part of which is a benefit unit and the other part of which is not "
                     "\n "
                     "\n 4: Explain family unit "
                     "\n 5: Explain benefit unit \n")

        match type:
            case "1":
                self.benefit_unit()
            case "2":
                self.family_unit()
            case "3":
                self.family_unit()
            case "4":
                self.family_unit_explanation()
            case "5":
                self.benefit_unit_explanation()
            case _:
                print("Please conduct more research")

    def family_unit(self):
        ans = input("Is your client part of a family unit that is not, and no part of which is, a benefit unit? \n Yes or No \n")
        if(ans == "Yes" or "yes" or "y" or "Y"):
            self.family_unit_size_determination()

    def benefit_unit(self):
        return True

    def family_unit_explanation(self):
        print(" Family unit means:"
              "\n An individual, the individual’s spouse and all of the children of both or either of them who are living with them,"
                "\n An individual and the individual’s spouse living with him or her, if neither has any children."
                "\n An individual and the individual’s children living with him or her, if the individual has no spouse, or"
                "\n An individual, if the individual has no spouse and no children \n")

        self.print_type_of_household()

    def benefit_unit_explanation(self):
        print("“Benefit Unit” means a benefit unit under the Ontario Works Act, 1997 or the Ontario Disability Support Program Act, 1997."
              "\n Under the Ontario Works Act, 1997 “benefit unit” means a person and all of his or her dependants on behalf of whom the person applies for or receives basic financial assistance. \n")

        self.print_type_of_household()

    def family_unit_size_determination(self):
        user_input_9 = input("Please specify the size of the family unit (number of individuals) \n")
        self.adjusted_family_net_income_calcuation()

    def adjusted_family_net_income_calcuation(self):
        print("Please provide the net income of each member of the family unit, excluding members who are in full-time attendance at a recognized educational facility")
        print("“recognized educational institution” means: "
              "\n(a) A school, as defined in the Education Act,"
                "\n (b)	A university,"
                "\n (c)	A college of applied arts and technology established under the Ontario Colleges of Applied Arts and Technology Act, 2002,"
                "\n (d)	A career college, as defined in the Ontario Career Colleges Act, 2005, or"
                "\n (e)	A private school, as defined in the Education Act, for which a notice of intention to operate has been submitted to the Ministry of Education in accordance with that Act.")
        net_income = float(input("Net Income = "))

        ans = input("What is the purpose of conducting the rental Calculation:"
                    "\n 1: Calculation is done for an Initial Calculation"
                    "\n 2: Calculation is done for the purposes of an Annual Review"
                    "\n 3: Calculation is done for the purposes of an In-Year Review \n")

        match ans:
            case "1":
               self.calculation_6_2(net_income)

            case "2":
                self.calculation_6_3()
            case "3":
                self.calculation_6_5(net_income)

    def calculation_6_2(self, net_income):
        recived_payment1 = float(input(
            "Input the total amount of all payments from a registered disability savings plan received by the member in that taxation year: "))
        repaid_payment = float(input("Input the total amount of all payments from a registered disability savings plan repaid by the member in that taxation year: "))

        NIBX = net_income - (recived_payment1 + repaid_payment)

        print(f"Net income of Member is:   {round(NIBX,2)}")

    def calculation_6_3(self):
        annual_review_date = input("When is the Annual Review being conducted?"
              "\n (YYYY-MM-DD): ")
        self.date_in_range(annual_review_date)
        recieved_saving = float(input("Input the total amount of all payments from a registered disability savings plan received by the member in that taxation year: "))
        amount_of_all_payments = float(input("Input the total amount of all payments from a registered disability savings plan repaid by the member in that taxation year: "))

        NIBX =  self.latest_notice_amm - recieved_saving + amount_of_all_payments
        print("Net income of Member is: " + str(round(NIBX, 2)))


    def date_in_range(self, annual_review_date):
        date = datetime.strptime(annual_review_date, '%Y-%m-%d')

        range_1_start = datetime(date.year, 1, 1)
        range_1_end = datetime(date.year, 6, 30)
        range_2_start = datetime(date.year, 7, 1)
        range_2_end = datetime(date.year, 12, 31)

        if(range_1_start <= date <= range_1_end):
            self.latest_notice_amm = float(input("Input the amount on the latest notice of assessment issued under the Income Tax Act (Canada) for the member’s taxation year IMMEDIATELY PRECEDING last December:"))
        elif(range_2_start <= date <= range_2_end):
            self.latest_notice_amm = float(input("Input the amount on the latest notice of assessment issued under the Income Tax Act (Canada) for the member’s most recent taxation year that ended BEFORE the beginning of the month in which the review is commenced: "))


    def calculation_6_5(self, net_income):
        NIBX = net_income

        print("Net income is " + str(NIBX))



# To start the application:
if __name__ == "__main__":
    app = Application()
