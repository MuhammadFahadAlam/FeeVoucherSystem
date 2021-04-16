"""
It will Generate Vouchers for the students

"""

try :
    import reportlab
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4, landscape
    
except:
    print("Missing One required module")
    print("Install reportlab module first. To install it copy this command in command prompt")
    print("pip install reportlab")

        
class Generate_Voucher ( ):
    """
    This is a class which generates a pdf

    This pdf is a Voucher and is using data from the Fields present
     in UserInterface File
    """

    def __init__( self , Name , F_Name , Roll_No , Class , Fee_month , Tuition , Examination , Total , Issue , Due  ):

        self.Name = Name
        self.F_Name = F_Name
        self.Roll_No = Roll_No
        self.Class = Class
        self.Fee_month = Fee_month
        self.Tuition = Tuition
        self.Examination = Examination
        self.Total = Total
        self.Issue = Issue
        self.Due = Due
        
        self.canvas = canvas.Canvas("Fee_Voucher%s.pdf"%(Roll_No))
        self.canvas.setPageSize ( landscape( A4 ) )                 #       Resolution of one copy of Voucher     
        self.generate( 0 , 'Student')                                          #                        595 x 842
        self.generate( 260 , '  Bank')
        self.generate( 520 , ' School')
        self.canvas.showPage( )
        self.canvas.save( )

    def generate( self , a , copy ):
        """
        This function is generating One copy of Voucher
        """
        
        self.canvas.rect(30+a , 35 , 260 , 520 , stroke=1, fill=0)

        self.canvas.drawString( 109+a ,510,"Kakashi Bolts")
        
        self.canvas.rect(109+a , 480 , 100 , 20 , stroke=1, fill=0)

        self.canvas.drawString( 119+a ,487,"%s Copy"%(copy))
        self.canvas.drawString( 39+a ,455,"Student Name")
        self.canvas.drawString( 139+a ,455,"%s"%(self.Name))
        self.canvas.drawString( 39+a ,435,"Father's Name")
        self.canvas.drawString( 139+a ,435,"%s"%(self.F_Name))
        self.canvas.drawString( 39+a ,415,"Roll No")
        self.canvas.drawString( 139+a ,415,"%s"%(self.Roll_No))
        self.canvas.drawString( 39+a ,395,"Class")
        self.canvas.drawString( 139+a ,395,"%s"%(self.Class))
        self.canvas.drawString( 39+a ,375,"Fee of Month")
        self.canvas.drawString( 139+a ,375,"%s"%(self.Fee_month))
        self.canvas.rect(39+a , 235 , 240 , 120 , stroke=1, fill=0)

        self.canvas.drawString( 59+a ,335,"Description")
        self.canvas.drawString( 199+a ,335,"Amount")

        self.canvas.rect(39+a , 235 , 240 , 90 , stroke=1, fill=0)

        self.canvas.drawString( 59+a ,295,"Tuition Fee")
        self.canvas.drawString( 59+a ,275,"Examination Fee")
        self.canvas.drawString( 59+a ,255,"Total Fee")

        self.canvas.drawString( 159+a ,295,"%s"%(self.Tuition))
        self.canvas.drawString( 159+a ,275,"%s"%(self.Examination))
        self.canvas.drawString( 159+a ,255,"%s"%(self.Total))

        self.canvas.drawString( 39+a ,210,"Issue Date :")
        self.canvas.drawString( 139+a ,210,"%s"%(self.Issue))
        self.canvas.drawString( 39+a ,195,"Due Date :")
        self.canvas.drawString( 139+a ,195,"%s"%(self.Due))

        self.canvas.rect(39+a , 100 , 240 , 80 , stroke=1, fill=0)

        self.canvas.drawString( 59+a , 160,"Bank Stamp :")

        self.canvas.drawString( 39+a ,80,"Note :")

        self.textobject = self.canvas.beginText( )
        self.textobject.setTextOrigin(69+a, 65)
        
        self.textobject.textLine( text = 'Fine of Rs. 15/- per day would be ' )
        self.textobject.textLine( text = 'charged in case of late payment.' )

        self.canvas.drawText( self.textobject )

        
