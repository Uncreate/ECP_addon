from tkinter import *
from tkinter import ttk


root = Tk()
root.title("ECP Addon")
root.geometry('1200x1000+50+50')

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fieldbackground="#D3D3D3")
    
style.map('Treeview',
    background=[('selected', "#347083")])

tree_frame = Frame(root)
tree_frame.pack(pady=(10,0))


tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree_scrollh = Scrollbar(tree_frame, orient='horizontal')
tree_scrollh.pack(side=BOTTOM, fill=X)

my_tree =ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set,xscrollcommand=tree_scrollh.set, selectmode="extended")
my_tree.pack()

tree_scroll.config(command=my_tree.yview)
tree_scrollh.config(command=my_tree.xview)


my_tree['columns'] = ("Ignore", "SoflexRule", "MillRule", "DrillRule", "Seq", "Crib_FR", "Crib_AZ", "Type", "EssaiPartNum", "EDPNum", "Description", "ThreadDescription11", "Diameter", "ShankDiameter", "ShoulderDiameter", "ShoulderLength", "ShoulderLenEnd", "ShoulderAngle", "MinOHL", "NumFlutes", "OAL", "LOC", "CornerRadius", "ThreadPitch", "ThreadClass", "TipAngle", "TipHeight", "TipDiameter", "ChamferLength", "Startshoulderlength", "ToolMaterial", "COATING", "Manufacturer", "NOTE", "AL", "S1", "CU", "PL", "PG", "ROUGH", "FIN", "ShapeName", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Ignore", anchor=W, width=45)
my_tree.column("SoflexRule", anchor=W, width=60)
my_tree.column("MillRule", anchor=W, width=50)
my_tree.column("DrillRule", anchor=W, width=50)
my_tree.column("Seq", anchor=W, width=50)
my_tree.column("Crib_FR", anchor=W, width=40)
my_tree.column("Crib_AZ", anchor=W, width=40)
my_tree.column("Type", anchor=W, width=40)
my_tree.column("EssaiPartNum", anchor=W, width=100)
my_tree.column("EDPNum", anchor=W, width=100)
my_tree.column("Description", anchor=W, width=100)
my_tree.column("ThreadDescription11", anchor=W, width=100)
my_tree.column("Diameter", anchor=W, width=140)
my_tree.column("ShankDiameter", anchor=W, width=140)
my_tree.column("ShoulderDiameter", anchor=W, width=140)
my_tree.column("ShoulderLength", anchor=W, width=140)
my_tree.column("ShoulderLenEnd", anchor=W, width=140)
my_tree.column("ShoulderAngle", anchor=W, width=140)
my_tree.column("MinOHL", anchor=W, width=140)
my_tree.column("NumFlutes", anchor=W, width=140)
my_tree.column("OAL", anchor=W, width=140)
my_tree.column("LOC", anchor=W, width=140)
my_tree.column("CornerRadius", anchor=W, width=140)
my_tree.column("ThreadPitch", anchor=W, width=140)
my_tree.column("ThreadClass", anchor=W, width=140)
my_tree.column("TipAngle", anchor=W, width=140)
my_tree.column("TipHeight", anchor=W, width=140)
my_tree.column("TipDiameter", anchor=W, width=140)
my_tree.column("ChamferLength", anchor=W, width=140)
my_tree.column("Startshoulderlength", anchor=W, width=140)
my_tree.column("ToolMaterial", anchor=W, width=140)
my_tree.column("COATING", anchor=W, width=140)
my_tree.column("Manufacturer", anchor=W, width=140)
my_tree.column("NOTE", anchor=W, width=140)
my_tree.column("AL", anchor=W, width=140)
my_tree.column("S1", anchor=W, width=140)
my_tree.column("CU", anchor=W, width=140)
my_tree.column("PL", anchor=W, width=140)
my_tree.column("PG", anchor=W, width=140)
my_tree.column("ROUGH", anchor=W, width=140)
my_tree.column("FIN", anchor=W, width=140)
my_tree.column("ShapeName", anchor=W, width=140)
my_tree.column("A", anchor=W, width=140)
my_tree.column("B", anchor=W, width=140)
my_tree.column("C", anchor=W, width=140)
my_tree.column("D", anchor=W, width=140)
my_tree.column("E", anchor=W, width=140)
my_tree.column("F", anchor=W, width=140)
my_tree.column("G", anchor=W, width=140)
my_tree.column("H", anchor=W, width=140)
my_tree.column("I", anchor=W, width=140)
my_tree.column("J", anchor=W, width=140)
my_tree.column("K", anchor=W, width=140)
my_tree.column("L", anchor=W, width=140)
my_tree.column("M", anchor=W, width=140)
my_tree.column("N", anchor=W, width=140)
my_tree.column("O", anchor=W, width=140)
my_tree.column("P", anchor=W, width=140)
my_tree.column("Q", anchor=W, width=140)
my_tree.column("R", anchor=W, width=140)


my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Ignore", text="Ignore", anchor=W)
my_tree.heading("SoflexRule", text="SoflexRule", anchor=W)
my_tree.heading("MillRule", text="MillRule", anchor=W)
my_tree.heading("DrillRule", text="DrillRule", anchor=W)
my_tree.heading("Seq", text="Seq #", anchor=W)
my_tree.heading("Crib_FR", text="Crib_FR", anchor=W)
my_tree.heading("Crib_AZ", text="Crib_AZ", anchor=W)
my_tree.heading("Type", text="Type", anchor=W)
my_tree.heading("EssaiPartNum", text="EssaiPartNum", anchor=W)
my_tree.heading("EDPNum", text="EDPNum", anchor=W)
my_tree.heading("Description", text="Description", anchor=W)
my_tree.heading("ThreadDescription11", text="ThreadDescription11", anchor=W)
my_tree.heading("Diameter", text="Diameter", anchor=W)
my_tree.heading("ShankDiameter", text="ShankDiameter", anchor=W)
my_tree.heading("ShoulderDiameter", text="ShoulderDiameter", anchor=W)
my_tree.heading("ShoulderLength", text="ShoulderLength", anchor=W)
my_tree.heading("ShoulderLenEnd", text="ShoulderLenEnd", anchor=W)
my_tree.heading("ShoulderAngle", text="ShoulderAngle", anchor=W)
my_tree.heading("MinOHL", text="MinOHL", anchor=W)
my_tree.heading("NumFlutes", text="NumFlutes", anchor=W)
my_tree.heading("OAL", text="OAL", anchor=W)
my_tree.heading("LOC", text="LOC", anchor=W)
my_tree.heading("CornerRadius", text="CornerRadius", anchor=W)
my_tree.heading("ThreadPitch", text="ThreadPitch", anchor=W)
my_tree.heading("ThreadClass", text="ThreadClass", anchor=W)
my_tree.heading("TipAngle", text="TipAngle", anchor=W)
my_tree.heading("TipHeight", text="TipHeight", anchor=W)
my_tree.heading("TipDiameter", text="TipDiameter", anchor=W)
my_tree.heading("ChamferLength", text="ChamferLength", anchor=W)
my_tree.heading("Startshoulderlength", text="Startshoulderlength", anchor=W)
my_tree.heading("ToolMaterial", text="ToolMaterial", anchor=W)
my_tree.heading("COATING", text="COATING", anchor=W)
my_tree.heading("Manufacturer", text="Manufacturer", anchor=W)
my_tree.heading("NOTE", text="NOTE", anchor=W)
my_tree.heading("AL", text="AL", anchor=W)
my_tree.heading("S1", text="S1", anchor=W)
my_tree.heading("CU", text="CU", anchor=W)
my_tree.heading("PL", text="PL", anchor=W)
my_tree.heading("PG", text="PG", anchor=W)
my_tree.heading("ROUGH", text="ROUGH", anchor=W)
my_tree.heading("FIN", text="FIN", anchor=W)
my_tree.heading("ShapeName", text="ShapeName", anchor=W)
my_tree.heading("A", text="A", anchor=W)
my_tree.heading("B", text="B", anchor=W)
my_tree.heading("C", text="C", anchor=W)
my_tree.heading("D", text="D", anchor=W)
my_tree.heading("E", text="E", anchor=W)
my_tree.heading("F", text="F", anchor=W)
my_tree.heading("G", text="G", anchor=W)
my_tree.heading("H", text="H", anchor=W)
my_tree.heading("I", text="I", anchor=W)
my_tree.heading("J", text="J", anchor=W)
my_tree.heading("K", text="K", anchor=W)
my_tree.heading("L", text="L", anchor=W)
my_tree.heading("M", text="M", anchor=W)
my_tree.heading("N", text="N", anchor=W)
my_tree.heading("O", text="O", anchor=W)
my_tree.heading("P", text="P", anchor=W)
my_tree.heading("Q", text="Q", anchor=W)
my_tree.heading("R", text="R", anchor=W)


data = [
    [0,"DR", "","DR",1333,"","X","CD","800-500006-09A","101 W161","CD .0063 2FL","",0.0062992125984252,0.125,0.0325,0.378,'',0,0.8,2,1.5,0.0590551181102362,'',"","",130,0.00146868553749606,'','','',"C","CT00","Union Tool","Circuit Brd.",1,0,1,1,1,1,1,"0.0063 Dia x 0..059 LOC - 2FLT CD x 130 Deg",0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [1,"EM", "EM","",1332,"","X","EM","800-500006-09A","102 W161","CD .0063 2FL","",1.00629921259843,1.125,1.0325,1.378,'',1,1.8,3,2.5,1.05905511811024,'',"","",131,1.0014686855375,'','','',"C","CT01","Union Tool","Circuit Brd.",2,1,2,2,2,2,2,"0.0063 Dia x 0..059 LOC - 2FLT CD x 130 Deg",1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1],
    [1,"EM", "EM","",1331,"","X","EM","800-500006-09A","103 W161","CD .0063 2FL","",2.00629921259843,2.125,2.0325,2.378,'',2,2.8,4,3.5,2.05905511811024,'',"","",132,2.0014686855375,'','','',"C","CT02","Union Tool","Circuit Brd.",3,2,3,3,3,3,3,"0.0063 Dia x 0..059 LOC - 2FLT CD x 130 Deg",2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2],
    [1,"EM", "EM","",1330,"","X","EM","800-500006-09A","104 W161","CD .0063 2FL","",3.00629921259843,3.125,3.0325,3.378,'',3,3.8,5,4.5,3.05905511811024,'',"","",133,3.0014686855375,'','','',"C","CT03","Union Tool","Circuit Brd.",4,3,4,4,4,4,4,"0.0063 Dia x 0..059 LOC - 2FLT CD x 130 Deg",3,3,3,3,3,3,3,3,4,3,3,3,3,3,3,3,3,3],
    [1,"CM", "CM","",1329,"","X","CM","800-500006-09A","105 W161","CD .0063 2FL","",4.00629921259843,4.125,4.0325,4.378,'',4,4.8,6,5.5,4.05905511811024,'',"","",134,4.0014686855375,'','','',"C","CT04","Union Tool","Circuit Brd.",5,4,5,5,5,5,5,"0.0063 Dia x 0..059 LOC - 2FLT CD x 130 Deg",4,4,4,4,4,4,4,4,5,4,4,4,4,4,4,4,4,4],
    [1,"SD", "","SD",1328,"","X","SD","800-500006-09A","106 W161","CD .0063 2FL","",5.00629921259843,5.125,5.0325,5.378,'',5,5.8,7,6.5,5.05905511811024,'',"","",135,5.0014686855375,'','','',"C","CT05","Union Tool","Circuit Brd.",6,5,6,6,6,6,6,"0.0063 Dia x 0..059 LOC - 2FLT CD x 130 Deg",5,5,5,5,5,5,5,5,6,5,5,5,5,5,5,5,5,5],
    [1,"EM", "EM","",1327,"","X","EM","800-500006-09A","107 W161","CD .0063 2FL","",6.00629921259843,6.125,6.0325,6.378,'',6,6.8,8,7.5,6.05905511811024,'',"","",136,6.0014686855375,'','','',"C","CT06","Union Tool","Circuit Brd.",7,6,7,7,7,7,7,"0.0063 Dia x 0..059 LOC - 2FLT CD x 130 Deg",6,6,6,6,6,6,6,6,7,6,6,6,6,6,6,6,6,6],
    [1,"EM", "EM","",1326,"","X","EM","800-500006-09A","108 W161","CD .0063 2FL","",7.00629921259843,7.125,7.0325,7.378,'',7,7.8,9,8.5,7.05905511811024,'',"","",137,7.0014686855375,'','','',"C","CT07","Union Tool","Circuit Brd.",8,7,8,8,8,8,8,"0.0063 Dia x 0..059 LOC - 2FLT CD x 130 Deg",7,7,7,7,7,7,7,7,8,7,7,7,7,7,7,7,7,7],
    [1,"SD", "","SD",1325,"","X","SD","800-500006-09A","109 W161","CD .0063 2FL","",8.00629921259842,8.125,8.0325,8.378,'',8,8.8,10,9.5,8.05905511811024,'',"","",138,8.0014686855375,'','','',"C","CT08","Union Tool","Circuit Brd.",9,8,9,9,9,9,9,"0.0063 Dia x 0..059 LOC - 2FLT CD x 130 Deg",8,8,8,8,8,8,8,8,9,8,8,8,8,8,8,8,8,8],
    [1,"DR", "","DR",1324,"","X","CD","800-500006-09A","110 W161","CD .0063 2FL","",9.00629921259842,9.125,9.0325,9.378,'',9,9.8,11,10.5,9.05905511811024,'',"","",139,9.0014686855375,'','','',"C","CT09","Union Tool","Circuit Brd.",10,9,10,10,10,10,10,"0.0063 Dia x 0..059 LOC - 2FLT CD x 130 Deg",9,9,9,9,9,9,9,9,10,9,9,9,9,9,9,9,9,9]

 ]

my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")



global count
count = 0

for record in data:
    if count % 2 ==0:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0],	record[1],	record[2],	record[3],	record[4],	record[5],	record[6],	record[7],	record[8],	record[9],	record[10],	record[11],	record[12],	record[13],	record[14],	record[15],	record[16],	record[17],	record[18],	record[19],	record[20],	record[21],	record[22],	record[23],	record[24],	record[25],	record[26],	record[27],	record[28],	record[29],	record[30],	record[31],	record[32],	record[33],	record[34],	record[35],	record[36],	record[37],	record[38],	record[39],	record[40],	record[41],	record[42],	record[43],	record[44],	record[45],	record[46],	record[47],	record[48],	record[49],	record[50],	record[51],	record[52],	record[53],	record[54],	record[55],	record[56],	record[57],	record[58],	record[59]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0],	record[1],	record[2],	record[3],	record[4],	record[5],	record[6],	record[7],	record[8],	record[9],	record[10],	record[11],	record[12],	record[13],	record[14],	record[15],	record[16],	record[17],	record[18],	record[19],	record[20],	record[21],	record[22],	record[23],	record[24],	record[25],	record[26],	record[27],	record[28],	record[29],	record[30],	record[31],	record[32],	record[33],	record[34],	record[35],	record[36],	record[37],	record[38],	record[39],	record[40],	record[41],	record[42],	record[43],	record[44],	record[45],	record[46],	record[47],	record[48],	record[49],	record[50],	record[51],	record[52],	record[53],	record[54],	record[55],	record[56],	record[57],	record[58],	record[59]), tags=('oddrow',))
    count +=1

data_frame = LabelFrame(root, text="Records")
data_frame.pack(fill="x", expand="yes", padx=20)


Ignore_label = Label(data_frame, text="Ignore")
Ignore_label.grid(row=0, column=0, pady=(10,0))
Ignore = Entry(data_frame, width=30)
Ignore.grid(row=0, column=1, padx=20, pady=(10,0))
Ignore.focus()

SoflexRule = ttk.Combobox(data_frame, width=28)
SoflexRule['values']= ("CM", "DR", "EM", "FM", "KC", "RM", "RT", "SD", "TE", "TM", "")
SoflexRule.grid(row=1, column=1)
MillRule = ttk.Combobox(data_frame, width=28)
MillRule['values']=("BA", "EM", "BU", "CM", "FM_CHMF", "FM_CR", "TE", "KC", "DA", "TM", "")
MillRule.grid(row=2, column=1)
DrillRule = ttk.Combobox(data_frame, width=28)
DrillRule['values']=("DR", "RM", "SD", "RT", "")
DrillRule.grid(row=3, column=1)
Seq = Entry(data_frame, width=30)
Seq.grid(row=4, column=1)
Crib_FR = ttk.Combobox(data_frame, width=28)
Crib_FR['values']=("X","")
Crib_FR.grid(row=5, column=1)
Crib_AZ = ttk.Combobox(data_frame, width=28)
Crib_AZ['values']=("X", "")
Crib_AZ.grid(row=6, column=1)
Type = ttk.Combobox(data_frame, width=28)
Type['values']=("EM", "BA", "BU", "LP", "FM", "DO", "CM", "CR", "DA", "KC", "SS", "SD", "CS", "DS", "DJ", "DT", "CD", "RM", "CT", "RT", "TM", "DC", "TE")
Type.grid(row=7, column=1)
EssaiPartNumber = Entry(data_frame, width=30)
EssaiPartNumber.grid(row=8, column=1)
EDPNum = Entry(data_frame, width=30)
EDPNum.grid(row=9, column=1)
Description = Entry(data_frame, width=30)
Description.grid(row=10, column=1)
ThreadDescription11 = Entry(data_frame, width=30)
ThreadDescription11.grid(row=11, column=1)
Diameter = Entry(data_frame, width=30)
Diameter.grid(row=12, column=1)
ShankDiameter = Entry(data_frame, width=30)
ShankDiameter.grid(row=13, column=1)
ShoulderDiameter = Entry(data_frame, width=30)
ShoulderDiameter.grid(row=14, column=1)
ShoulderLength = Entry(data_frame, width=30)
ShoulderLength.grid(row=15, column=1)
ShoulderLenEnd = Entry(data_frame, width=30)
ShoulderLenEnd.grid(row=16, column=1)
ShoulderAngle = Entry(data_frame, width=30)
ShoulderAngle.grid(row=17, column=1)
MinOHL = Entry(data_frame, width=30)
MinOHL.grid(row=18, column=1)
NumFlutes = Entry(data_frame, width=30)
NumFlutes.grid(row=19, column=1)
OAL = Entry(data_frame, width=30)
OAL.grid(row=0, column=3, padx=20, pady=(10,0))
LOC = Entry(data_frame, width=30)
LOC.grid(row=1, column=3)
CornerRadius = Entry(data_frame, width=30)
CornerRadius.grid(row=2, column=3)
ThreadPitch = Entry(data_frame, width=30)
ThreadPitch.grid(row=3, column=3)
ThreadClass = Entry(data_frame, width=30)
ThreadClass.grid(row=4, column=3)
TipAngle = Entry(data_frame, width=30)
TipAngle.grid(row=5, column=3)
TipHeight = Entry(data_frame, width=30)
TipHeight.grid(row=6, column=3)
TipDiameter = Entry(data_frame, width=30)
TipDiameter.grid(row=7, column=3)
ChamferLength = Entry(data_frame, width=30)
ChamferLength.grid(row=8, column=3)
Startshoulderlength = Entry(data_frame, width=30)
Startshoulderlength.grid(row=9, column=3)
ToolMaterial = Entry(data_frame, width=30)
ToolMaterial.grid(row=10, column=3)
COATING = Entry(data_frame, width=30)
COATING.grid(row=11, column=3)
Manufacturer = Entry(data_frame, width=30)
Manufacturer.grid(row=12, column=3)
NOTE = Entry(data_frame, width=30)
NOTE.grid(row=13, column=3)
# Make into check boxes
AL = ttk.Combobox(data_frame, width=28)
AL['values']=("0","1")
AL.grid(row=14, column=3)
CU = ttk.Combobox(data_frame, width=28)
CU['values']=("0","1")
CU.grid(row=15, column=3)
PG = ttk.Combobox(data_frame, width=28)
PG['values']=("0","1")
PG.grid(row=16, column=3)
PL = ttk.Combobox(data_frame, width=28)
PL['values']=("0","1")
PL.grid(row=17, column=3)
S1 = ttk.Combobox(data_frame, width=28)
S1['values']=("0","1")
S1.grid(row=18, column=3)
ROUGH = Entry(data_frame, width=30)
ROUGH.grid(row=19, column=3)
FIN = Entry(data_frame, width=30)
FIN.grid(row=0, column=5, padx=20, pady=(10,0))
ShapeName = Entry(data_frame, width=30)
ShapeName.grid(row=1, column=5)

A = Entry(data_frame, width=30)
A.grid(row=2, column=5)
B1= IntVar()
B = Entry(data_frame, width=30)
B.grid(row=3, column=5)
C1= IntVar()
C = Entry(data_frame, width=30)
C.grid(row=4, column=5)
D1= IntVar()
D = Entry(data_frame, width=30)
D.grid(row=5, column=5)
E1=IntVar()
E = Entry(data_frame, width=30)
E.grid(row=6, column=5)
F1=IntVar()
F = Entry(data_frame, width=30)
F.grid(row=7, column=5)
G1=IntVar()
G = Entry(data_frame, width=30)
G.grid(row=8, column=5)
H1=IntVar()
H = Entry(data_frame, width=30)
H.grid(row=9, column=5)
I1=IntVar()
I = Entry(data_frame, width=30)
I.grid(row=10, column=5)
J1=IntVar()
J = Entry(data_frame, width=30)
J.grid(row=11, column=5)
K1=IntVar()
K = Entry(data_frame, width=30)
K.grid(row=12, column=5)
L1=IntVar()
L = Entry(data_frame, width=30)
L.grid(row=13, column=5)
M1=IntVar()
M = Entry(data_frame, width=30)
M.grid(row=14, column=5)
N1=IntVar()
N = Entry(data_frame, width=30)
N.grid(row=15, column=5)
O1=IntVar()
O = Entry(data_frame, width=30)
O.grid(row=16, column=5)
P1=IntVar()
P = Entry(data_frame, width=30)
P.grid(row=17, column=5)
Q1=IntVar()
Q = Entry(data_frame, width=30)
Q.grid(row=18, column=5)
R1=IntVar()
R = Entry(data_frame, width=30)
R.grid(row=19, column=5)

# Create Labels

SoflexRule_label = Label(data_frame, text="Soflex Rule")
SoflexRule_label.grid(row=1, column=0)
MillRule_label = Label(data_frame, text="Mill Rule")
MillRule_label.grid(row=2, column=0)
DrillRule_label = Label(data_frame, text="Drill Rule")
DrillRule_label.grid(row=3, column=0)
Seq_label = Label(data_frame, text="Sequence Number")
Seq_label.grid(row=4, column=0)
Crib_FR_label = Label(data_frame, text="Freemont Crib")
Crib_FR_label.grid(row=5, column=0)
Crib_AZ_label = Label(data_frame, text="Arizona Crib")
Crib_AZ_label.grid(row=6, column=0)
Type_label = Label(data_frame, text="Type")
Type_label.grid(row=7, column=0)
EssaiPartNumber_label = Label(data_frame, text="Essai Part Number")
EssaiPartNumber_label.grid(row=8, column=0)
EDPNum_label = Label(data_frame, text="EDP Number")
EDPNum_label.grid(row=9, column=0)
Description_label = Label(data_frame, text="Description")
Description_label.grid(row=10, column=0)
ThreadDescription11_label = Label(data_frame, text="Thread Description")
ThreadDescription11_label.grid(row=11, column=0)
Diameter_label = Label(data_frame, text="Diameter")
Diameter_label.grid(row=12, column=0)
ShankDiameter_label = Label(data_frame, text="Shank Diameter")
ShankDiameter_label.grid(row=13, column=0)
ShoulderDiameter_label = Label(data_frame, text="Shoulder Diameter")
ShoulderDiameter_label.grid(row=14, column=0)
ShoulderLength_label = Label(data_frame, text="Shoulder Length")
ShoulderLength_label.grid(row=15, column=0)
ShoulderLenEnd_label = Label(data_frame, text="Shoulder Length End")
ShoulderLenEnd_label.grid(row=16, column=0)
ShoulderAngle_label = Label(data_frame, text="Shoulder Angle")
ShoulderAngle_label.grid(row=17, column=0)
MinOHL_label = Label(data_frame, text="Minimum OHL")
MinOHL_label.grid(row=18, column=0)
NumFLutes_label = Label(data_frame, text="Number of Flutes")
NumFLutes_label.grid(row=19, column=0)
OAL_label = Label(data_frame, text="Overall Length")
OAL_label.grid(row=0, column=2, padx=20, pady=(10,0))
LOC_label = Label(data_frame, text="Length of Cut")
LOC_label.grid(row=1, column=2)
CornerRadius_label = Label(data_frame, text="Corner Radius")
CornerRadius_label.grid(row=2, column=2)
ThreadPitch_label = Label(data_frame, text="Thread Pitch")
ThreadPitch_label.grid(row=3, column=2)
ThreadClass_label = Label(data_frame, text="Thread Class")
ThreadClass_label.grid(row=4, column=2)
TipAngle_label = Label(data_frame, text="Tip Angle")
TipAngle_label.grid (row=5, column=2)
TipHeight_label = Label(data_frame, text="Tip Height")
TipHeight_label.grid (row=6, column=2)
TipDiameter_label = Label(data_frame, text="Tip Diameter")
TipDiameter_label.grid (row=7, column=2)
ChamferLength_label = Label(data_frame, text="Chamfer Length")
ChamferLength_label.grid (row=8, column=2)
Startshoulderlength_label = Label(data_frame, text="Shoulder Length Start")
Startshoulderlength_label.grid (row=9, column=2)
ToolMaterial_label = Label(data_frame, text="Tool Material")
ToolMaterial_label.grid (row=10, column=2)
COATING_label = Label(data_frame, text="Coating")
COATING_label.grid (row=11, column=2)
Manufacturer_label = Label(data_frame, text="Manufacturer")
Manufacturer_label.grid (row=12, column=2)
NOTE_label = Label(data_frame, text="Note:")
NOTE_label.grid (row=13, column=2)
AL_label = Label(data_frame, text="Aluminum")
AL_label.grid (row=14, column=2)
CU_label = Label(data_frame, text="Copper")
CU_label.grid (row=15, column=2)
PG_label = Label(data_frame, text="Plastic Glass")
PG_label.grid (row=16, column=2)
PL_label = Label(data_frame, text="Plastic")
PL_label.grid (row=17, column=2)
S1_label = Label(data_frame, text="Stainless Steel")
S1_label.grid (row=18, column=2)
ROUGH_label = Label(data_frame, text="Rougher")
ROUGH_label.grid (row=19, column=2)
FIN_label = Label(data_frame, text="Finisher")
FIN_label.grid (row=0, column=4, padx=20, pady=(10,0))
ShapeName_label = Label(data_frame, text="Shape Name")
ShapeName_label.grid (row=1, column=4)
A_label = Label(data_frame, text="HSK50-ER16x100")
A_label.grid (row=2, column=4)
B_label = Label(data_frame, text="HSK50-ER32x100")
B_label.grid (row=3, column=4)
C_label = Label(data_frame, text="HSK50-PG10x100")
C_label.grid (row=4, column=4)
D_label = Label(data_frame, text="HSK63-ER11x100")
D_label.grid (row=5, column=4)
E_label = Label(data_frame, text="HSK63-ER16x100")
E_label.grid (row=6, column=4)
F_label = Label(data_frame, text="HSK63-ER16x160")
F_label.grid (row=7, column=4)
G_label = Label(data_frame, text="HSK63-ER20x75")
G_label.grid (row=8, column=4)
H_label = Label(data_frame, text="HSK63-ER32x100")
H_label.grid (row=9, column=4)
I_label = Label(data_frame, text="HSK63-PG10x100")
I_label.grid (row=10, column=4)
J_label = Label(data_frame, text="HSK63-PG10x120")
J_label.grid (row=11, column=4)
K_label = Label(data_frame, text="HSK63-PG15x100")
K_label.grid (row=12, column=4)
L_label = Label(data_frame, text="HSK63-PG15x120")
L_label.grid (row=13, column=4)
M_label = Label(data_frame, text="HSK63-PG15x160")
M_label.grid (row=14, column=4)
N_label = Label(data_frame, text="HSK63-PG25x100")
N_label.grid (row=15, column=4)
O_label = Label(data_frame, text="HSK63-PG32x100")
O_label.grid (row=16, column=4)
P_label = Label(data_frame, text="HSK63-SM075")
P_label.grid (row=17, column=4)
Q_label = Label(data_frame, text="HSK63-10SM2")
Q_label.grid (row=18, column=4)
R_label = Label(data_frame, text="HSK63-SM75-3.0")
R_label.grid (row=19, column=4)


# Select Record
def select_record():
    # Clear the form
    Ignore.delete(0, END),
    SoflexRule.delete(0, END),
    MillRule.delete(0, END),
    DrillRule.delete(0, END),
    Seq.delete(0, END),
    Crib_FR.delete(0, END),
    Crib_AZ.delete(0, END),
    Type.delete(0, END),
    EssaiPartNumber.delete(0, END),
    EDPNum.delete(0,END),
    Description.delete(0,END),
    ThreadDescription11.delete(0,END),
    Diameter.delete(0,END),
    ShankDiameter.delete(0,END),
    ShoulderDiameter.delete(0,END),
    ShoulderLength.delete(0,END),
    ShoulderLenEnd.delete(0,END),
    ShoulderAngle.delete(0,END),
    MinOHL.delete(0,END),
    NumFlutes.delete(0,END),
    OAL.delete(0,END),
    LOC.delete(0,END),
    CornerRadius.delete(0,END),
    ThreadPitch.delete(0,END),
    ThreadClass.delete(0,END),
    TipAngle.delete(0,END),
    TipHeight.delete(0,END),
    TipDiameter.delete(0,END),
    ChamferLength.delete(0,END),
    Startshoulderlength.delete(0,END),
    ToolMaterial.delete(0,END),
    COATING.delete(0,END),
    Manufacturer.delete(0,END),
    NOTE.delete(0,END),
    AL.delete(0, END),
    S1.delete(0, END),
    CU.delete(0, END),
    PL.delete(0, END),
    PG.delete(0, END),
    ROUGH.delete(0,END),
    FIN.delete(0,END),
    ShapeName.delete(0,END),
    A.delete(0, END),
    B.delete(0, END),
    C.delete(0, END),
    D.delete(0, END),
    E.delete(0, END),
    F.delete(0, END),
    G.delete(0, END),
    H.delete(0, END),
    I.delete(0, END),
    J.delete(0, END),
    K.delete(0, END),
    L.delete(0, END),
    M.delete(0, END),
    N.delete(0, END),
    O.delete(0, END),
    P.delete(0, END),
    Q.delete(0, END),
    R.delete(0, END),
    # Get Record Number
    selected = my_tree.focus()
    # Get Record Values
    values = my_tree.item(selected, 'values')
    # Fill the form
    Ignore.insert(0, values[0])
    SoflexRule.insert(0, values[1])
    MillRule.insert(0, values[2])
    DrillRule.insert(0, values[3])
    Seq.insert(0, values[4])
    Crib_FR.insert(0, values[5])
    Crib_AZ.insert(0, values[6])
    Type.insert(0, values[7])
    EssaiPartNumber.insert(0, values[8])
    EDPNum.insert(0, values[9])
    Description.insert(0, values[10])
    ThreadDescription11.insert(0, values[11])
    Diameter.insert(0, values[12])
    ShankDiameter.insert(0, values[13])
    ShoulderDiameter.insert(0, values[14])
    ShoulderLength.insert(0, values[15])
    ShoulderLenEnd.insert(0, values[16])
    ShoulderAngle.insert(0, values[17])
    MinOHL.insert(0, values[18])
    NumFlutes.insert(0, values[19])
    OAL.insert(0, values[20])
    LOC.insert(0, values[21])
    CornerRadius.insert(0, values[22])
    ThreadPitch.insert(0, values[23])
    ThreadClass.insert(0, values[24])
    TipAngle.insert(0, values[25])
    TipHeight.insert(0, values[26])
    TipDiameter.insert(0, values[27])
    ChamferLength.insert(0, values[28])
    Startshoulderlength.insert(0, values[29])
    ToolMaterial.insert(0, values[30])
    COATING.insert(0, values[31])
    Manufacturer.insert(0, values[32])
    NOTE.insert(0, values[33])
    AL.insert(0, values[34])
    S1.insert(0, values[35])
    CU.insert(0, values[36])
    PL.insert(0, values[37])
    PG.insert(0, values[38])
    ROUGH.insert(0, values[39])
    FIN.insert(0, values[40])
    ShapeName.insert(0, values[41])
    A.insert(0, values[42])
    B.insert(0, values[43])
    C.insert(0, values[44])
    D.insert(0, values[45])
    E.insert(0, values[46])
    F.insert(0, values[47])
    G.insert(0, values[48])
    H.insert(0, values[49])
    I.insert(0, values[50])
    J.insert(0, values[51])
    K.insert(0, values[52])
    L.insert(0, values[53])
    M.insert(0, values[54])
    N.insert(0, values[55])
    O.insert(0, values[56])
    P.insert(0, values[57])
    Q.insert(0, values[58])
    R.insert(0, values[59])
    
    
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

add_button = Button(button_frame, text="Add Tool")
add_button.grid(row=0, column=0, padx=10, pady=10)

update_button = Button(button_frame, text="Update Tool")
update_button.grid(row=0, column=1, padx=10, pady=10)

delete_button = Button(button_frame, text="Remove Tool")
delete_button.grid(row=0, column=2, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Selected Tools")
remove_many_button.grid(row=0, column=3, padx=10, pady=10)

select_button = Button(button_frame, text="Select Tool", command=select_record)
select_button.grid(row=0, column=4, padx=10, pady=10)

root.mainloop()
