from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import pandas as pd


root = Tk()
root.title("ECP Addon")
root.geometry('1200x900+50+50')



def lookup_records():
	global search_entry, search

	search = Toplevel(root)
	search.title("Lookup Tool")
	search.geometry("400x200")
	

	# Create label frame
	search_frame = LabelFrame(search, text="Essai Part Number")
	search_frame.pack(padx=10, pady=10)

	# Add entry box
	search_entry = Entry(search_frame, font=("Helvetica", 18))
	search_entry.pack(pady=20, padx=20)

	# Add button
	search_button = Button(search, text="Search Tools", command=search_records)
	search_button.pack(padx=20, pady=20)

def search_records():
        lookup_record = search_entry.get()
        # close the search box
        search.destroy()
        
        # Clear the Treeview
        for record in my_tree.get_children():
            my_tree.delete(record)
        
        # Create a database or connect to one that exists
        conn = sqlite3.connect('data/tools.db')

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM tools WHERE EssaiPartNum like ?", (lookup_record,))
        records = c.fetchall()
        
        # Add our data to the screen
        global count
        count = 0
        
        #for record in records:
        #	print(record)


        for record in records:
                if count % 2 ==0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1],	record[2],	record[3],	record[4],	record[0],	record[6],	record[7],	record[8],	record[9],	record[10],	record[11],	record[12],	record[13],	record[14],	record[15],	record[16],	record[17],	record[18],	record[19],	record[20],	record[21],	record[22],	record[23],	record[24],	record[25],	record[26],	record[27],	record[28],	record[29],	record[30],	record[31],	record[32],	record[33],	record[34],	record[35],	record[36],	record[37],	record[38],	record[39],	record[40],	record[41],	record[42],	record[43],	record[44],	record[45],	record[46],	record[47],	record[48],	record[49],	record[50],	record[51],	record[52],	record[53],	record[54],	record[55],	record[56],	record[57],	record[58],	record[59],	record[60]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1],	record[2],	record[3],	record[4],	record[0],	record[6],	record[7],	record[8],	record[9],	record[10],	record[11],	record[12],	record[13],	record[14],	record[15],	record[16],	record[17],	record[18],	record[19],	record[20],	record[21],	record[22],	record[23],	record[24],	record[25],	record[26],	record[27],	record[28],	record[29],	record[30],	record[31],	record[32],	record[33],	record[34],	record[35],	record[36],	record[37],	record[38],	record[39],	record[40],	record[41],	record[42],	record[43],	record[44],	record[45],	record[46],	record[47],	record[48],	record[49],	record[50],	record[51],	record[52],	record[53],	record[54],	record[55],	record[56],	record[57],	record[58],	record[59],	record[60]), tags=('oddrow',))
                count +=1


        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()



def BOM():
    cxn = sqlite3.connect('data/tools.db')
    wb = pd.read_excel('data/BOM.xlsx',sheet_name = 'Tools', keep_default_na=False)
    wb.to_sql(name='tools',con=cxn,if_exists='replace',index=False)
    cxn.commit()
    cxn.close()

def export_bom():
    conn = sqlite3.connect('data/tools.db')
    # pd.read_sql('SELECT * FROM tools',conn).to_excel('data/BOM.xlsx', sheet_name= 'Tools',float_format='%.4f',index= FALSE)
    wb = pd.read_sql('SELECT * FROM tools',conn)
    with pd.ExcelWriter('data/BOM.xlsx', mode='a', if_sheet_exists="replace") as writer:
        wb.to_excel(writer,sheet_name = 'Tools', index = FALSE)
    
def export_short_bom():
    conn = sqlite3.connect('data/tools.db')
    # pd.read_sql('SELECT * FROM tools',conn).to_excel('data/BOM.xlsx', sheet_name= 'Tools',float_format='%.4f',index= FALSE)
    wb = pd.read_sql('SELECT * FROM tools WHERE Ignore is 0',conn)
    with pd.ExcelWriter('data/BOM.xlsx', mode='a', if_sheet_exists="replace") as writer:
        wb.to_excel(writer,sheet_name = 'Tools', index = FALSE)

def query_database():
    # Just in case Clear the treeview (Search Reset)
    my_tree.delete(*my_tree.get_children())
    
    # Create or Connect to database
    conn = sqlite3.connect('data/tools.db')
    # DB Cursor
    c = conn.cursor()
    c.execute("SELECT rowid,* FROM tools")
    records = c.fetchall()
    global count
    count = 0
    
    for record in records:
        if count % 2 ==0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1],	record[2],	record[3],	record[4],	record[0],	record[6],	record[7],	record[8],	record[9],	record[10],	record[11],	record[12],	record[13],	record[14],	record[15],	record[16],	record[17],	record[18],	record[19],	record[20],	record[21],	record[22],	record[23],	record[24],	record[25],	record[26],	record[27],	record[28],	record[29],	record[30],	record[31],	record[32],	record[33],	record[34],	record[35],	record[36],	record[37],	record[38],	record[39],	record[40],	record[41],	record[42],	record[43],	record[44],	record[45],	record[46],	record[47],	record[48],	record[49],	record[50],	record[51],	record[52],	record[53],	record[54],	record[55],	record[56],	record[57],	record[58],	record[59],	record[60]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1],	record[2],	record[3],	record[4],	record[0],	record[6],	record[7],	record[8],	record[9],	record[10],	record[11],	record[12],	record[13],	record[14],	record[15],	record[16],	record[17],	record[18],	record[19],	record[20],	record[21],	record[22],	record[23],	record[24],	record[25],	record[26],	record[27],	record[28],	record[29],	record[30],	record[31],	record[32],	record[33],	record[34],	record[35],	record[36],	record[37],	record[38],	record[39],	record[40],	record[41],	record[42],	record[43],	record[44],	record[45],	record[46],	record[47],	record[48],	record[49],	record[50],	record[51],	record[52],	record[53],	record[54],	record[55],	record[56],	record[57],	record[58],	record[59],	record[60]), tags=('oddrow',))
        count +=1
        
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
tree_frame.pack(pady=20, padx=10)


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




my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")





data_frame = LabelFrame(root, text="Tool Information")
data_frame.pack(fill="x", expand="yes", padx=20)


Ignore_label = Label(data_frame, text="Ignore")
Ignore_label.grid(row=0, column=0,padx=(10,0))
Ignore = Entry(data_frame, width=17)
Ignore.grid(row=0, column=1, padx=20)
Ignore.focus()

SoflexRule_label = Label(data_frame, text="Soflex Rule")
SoflexRule_label.grid(row=1, column=0)
SoflexRule = ttk.Combobox(data_frame, width=15)
SoflexRule['values']= ("BA", "BU", "CM", "DR", "EM", "FM", "KC", "RM", "RT", "SD", "TE", "TM", "")
SoflexRule.grid(row=1, column=1)

MillRule_label = Label(data_frame, text="Mill Rule")
MillRule_label.grid(row=2, column=0)
MillRule = ttk.Combobox(data_frame, width=15)
MillRule['values']=("BA", "EM", "BU", "CM", "FM_CHMF", "FM_CR", "TE", "KC", "DA", "TM", "")
MillRule.grid(row=2, column=1)

DrillRule_label = Label(data_frame, text="Drill Rule")
DrillRule_label.grid(row=3, column=0)
DrillRule = ttk.Combobox(data_frame, width=15)
DrillRule['values']=("DR", "RM", "SD", "RT", "")
DrillRule.grid(row=3, column=1)

Seq_label = Label(data_frame, text="Sequence Number")
Seq_label.grid(row=4, column=0)
Seq = Entry(data_frame, width=17)
Seq.grid(row=4, column=1)

Crib_FR_label = Label(data_frame, text="Freemont Crib")
Crib_FR_label.grid(row=5, column=0)
Crib_FR = ttk.Combobox(data_frame, width=15)
Crib_FR['values']=("X","")
Crib_FR.grid(row=5, column=1)

Crib_AZ_label = Label(data_frame, text="Arizona Crib")
Crib_AZ_label.grid(row=6, column=0)
Crib_AZ = ttk.Combobox(data_frame, width=15)
Crib_AZ['values']=("X", "")
Crib_AZ.grid(row=6, column=1)

Type_label = Label(data_frame, text="Type")
Type_label.grid(row=7, column=0)
Type = ttk.Combobox(data_frame, width=15)
Type['values']=("EM", "BA", "BU", "LP", "FM", "DO", "CM", "CR", "DA", "KC", "SS", "SD", "CS", "DS", "DJ", "DT", "CD", "RM", "CT", "RT", "TM", "DC", "TE")
Type.grid(row=7, column=1)

EssaiPartNumber_label = Label(data_frame, text="Essai Part Number")
EssaiPartNumber_label.grid(row=8, column=0)
EssaiPartNumber = Entry(data_frame, width=17)
EssaiPartNumber.grid(row=8, column=1)

EDPNum_label = Label(data_frame, text="EDP Number")
EDPNum_label.grid(row=9, column=0)
EDPNum = Entry(data_frame, width=17)
EDPNum.grid(row=9, column=1)

Description_label = Label(data_frame, text="Description")
Description_label.grid(row=10, column=0)
Description = Entry(data_frame, width=17)
Description.grid(row=10, column=1)

ThreadDescription11_label = Label(data_frame, text="Thread Description")
ThreadDescription11_label.grid(row=11, column=0)
ThreadDescription11 = Entry(data_frame, width=17)
ThreadDescription11.grid(row=11, column=1)

Diameter_label = Label(data_frame, text="Diameter")
Diameter_label.grid(row=12, column=0)
Diameter = Entry(data_frame, width=17)
Diameter.grid(row=12, column=1)

ShankDiameter_label = Label(data_frame, text="Shank Diameter")
ShankDiameter_label.grid(row=13, column=0)
ShankDiameter = Entry(data_frame, width=17)
ShankDiameter.grid(row=13, column=1)

ShoulderDiameter_label = Label(data_frame, text="Shoulder Diameter")
ShoulderDiameter_label.grid(row=14, column=0)
ShoulderDiameter = Entry(data_frame, width=17)
ShoulderDiameter.grid(row=14, column=1)

ShoulderLength_label = Label(data_frame, text="Shoulder Length")
ShoulderLength_label.grid(row=15, column=0)
ShoulderLength = Entry(data_frame, width=17)
ShoulderLength.grid(row=15, column=1)

ShoulderLenEnd_label = Label(data_frame, text="Shoulder Length End")
ShoulderLenEnd_label.grid(row=0, column=2,padx=(10,0))
ShoulderLenEnd = Entry(data_frame, width=17)
ShoulderLenEnd.grid(row=0, column=3)

ShoulderAngle_label = Label(data_frame, text="Shoulder Angle")
ShoulderAngle_label.grid(row=1, column=2)
ShoulderAngle = Entry(data_frame, width=17)
ShoulderAngle.grid(row=1, column=3)

MinOHL_label = Label(data_frame, text="Minimum OHL")
MinOHL_label.grid(row=2, column=2)
MinOHL = Entry(data_frame, width=17)
MinOHL.grid(row=2, column=3)

NumFLutes_label = Label(data_frame, text="Number of Flutes")
NumFLutes_label.grid(row=3, column=2)
NumFlutes = Entry(data_frame, width=17)
NumFlutes.grid(row=3, column=3)

OAL_label = Label(data_frame, text="Overall Length")
OAL_label.grid(row=4, column=2)
OAL = Entry(data_frame, width=17)
OAL.grid(row=4, column=3)

LOC_label = Label(data_frame, text="Length of Cut")
LOC_label.grid(row=5, column=2)
LOC = Entry(data_frame, width=17)
LOC.grid(row=5, column=3)

CornerRadius_label = Label(data_frame, text="Corner Radius")
CornerRadius_label.grid(row=6, column=2)
CornerRadius = Entry(data_frame, width=17)
CornerRadius.grid(row=6, column=3)

ThreadPitch_label = Label(data_frame, text="Thread Pitch")
ThreadPitch_label.grid(row=7, column=2)
ThreadPitch = Entry(data_frame, width=17)
ThreadPitch.grid(row=7, column=3)

ThreadClass_label = Label(data_frame, text="Thread Class")
ThreadClass_label.grid(row=8, column=2)
ThreadClass = Entry(data_frame, width=17)
ThreadClass.grid(row=8, column=3)

TipAngle_label = Label(data_frame, text="Tip Angle")
TipAngle_label.grid (row=9, column=2)
TipAngle = Entry(data_frame, width=17)
TipAngle.grid(row=9, column=3)

TipHeight_label = Label(data_frame, text="Tip Height")
TipHeight_label.grid (row=10, column=2)
TipHeight = Entry(data_frame, width=17)
TipHeight.grid(row=10, column=3)

TipDiameter_label = Label(data_frame, text="Tip Diameter")
TipDiameter_label.grid (row=11, column=2)
TipDiameter = Entry(data_frame, width=17)
TipDiameter.grid(row=11, column=3)

ChamferLength_label = Label(data_frame, text="Chamfer Length")
ChamferLength_label.grid (row=12, column=2)
ChamferLength = Entry(data_frame, width=17)
ChamferLength.grid(row=12, column=3)

Startshoulderlength_label = Label(data_frame, text="Shoulder Length Start")
Startshoulderlength_label.grid (row=13, column=2)
Startshoulderlength = Entry(data_frame, width=17)
Startshoulderlength.grid(row=13, column=3)

ToolMaterial_label = Label(data_frame, text="Tool Material")
ToolMaterial_label.grid (row=14, column=2)
ToolMaterial = Entry(data_frame, width=17)
ToolMaterial.grid(row=14, column=3)

COATING_label = Label(data_frame, text="Coating")
COATING_label.grid (row=0, column=4,padx=(10,0))
COATING = Entry(data_frame, width=17)
COATING.grid(row=0, column=5)

Manufacturer_label = Label(data_frame, text="Manufacturer")
Manufacturer_label.grid (row=1, column=4)
Manufacturer = Entry(data_frame, width=17)
Manufacturer.grid(row=1, column=5)

NOTE_label = Label(data_frame, text="Note:")
NOTE_label.grid (row=2, column=4)
NOTE = Entry(data_frame, width=17)
NOTE.grid(row=2, column=5)
# Make into check boxes

AL_label = Label(data_frame, text="Aluminum")
AL_label.grid (row=3, column=4)
AL = ttk.Combobox(data_frame, width=15)
AL['values']=("0","1")
AL.grid(row=3, column=5)

CU_label = Label(data_frame, text="Copper")
CU_label.grid (row=4, column=4)
CU = ttk.Combobox(data_frame, width=15)
CU['values']=("0","1")
CU.grid(row=4, column=5)

PG_label = Label(data_frame, text="Plastic Glass")
PG_label.grid (row=5, column=4)
PG = ttk.Combobox(data_frame, width=15)
PG['values']=("0","1")
PG.grid(row=5, column=5)

PL_label = Label(data_frame, text="Plastic")
PL_label.grid (row=6, column=4)
PL = ttk.Combobox(data_frame, width=15)
PL['values']=("0","1")
PL.grid(row=6, column=5)

S1_label = Label(data_frame, text="Stainless Steel")
S1_label.grid (row=7, column=4)
S1 = ttk.Combobox(data_frame, width=15)
S1['values']=("0","1")
S1.grid(row=7, column=5)

ROUGH_label = Label(data_frame, text="Rougher")
ROUGH_label.grid (row=8, column=4)
ROUGH = Entry(data_frame, width=17)
ROUGH.grid(row=8, column=5)

FIN_label = Label(data_frame, text="Finisher")
FIN_label.grid (row=9, column=4)
FIN = Entry(data_frame, width=17)
FIN.grid(row=9, column=5)

ShapeName_label = Label(data_frame, text="Shape Name")
ShapeName_label.grid (row=10, column=4)
ShapeName = Entry(data_frame, width=17)
ShapeName.grid(row=10, column=5)

A_label = Label(data_frame, text="HSK50-ER16x100")
A_label.grid (row=11, column=4)
A = Entry(data_frame, width=17)
A.grid(row=11, column=5)

B_label = Label(data_frame, text="HSK50-ER32x100")
B_label.grid (row=12, column=4)
B = Entry(data_frame, width=17)
B.grid(row=12, column=5)

C_label = Label(data_frame, text="HSK50-PG10x100")
C_label.grid (row=13, column=4)
C = Entry(data_frame, width=17)
C.grid(row=13, column=5)

D_label = Label(data_frame, text="HSK63-ER11x100")
D_label.grid (row=14, column=4)
D = Entry(data_frame, width=17)
D.grid(row=14, column=5)

E_label = Label(data_frame, text="HSK63-ER16x100")
E_label.grid (row=0, column=6, padx=(10,0))
E = Entry(data_frame, width=17)
E.grid(row=0, column=7)

F_label = Label(data_frame, text="HSK63-ER16x160")
F_label.grid (row=1, column=6)
F = Entry(data_frame, width=17)
F.grid(row=1, column=7)

G_label = Label(data_frame, text="HSK63-ER20x75")
G_label.grid (row=2, column=6)
G = Entry(data_frame, width=17)
G.grid(row=2, column=7)

H_label = Label(data_frame, text="HSK63-ER32x100")
H_label.grid (row=3, column=6)
H = Entry(data_frame, width=17)
H.grid(row=3, column=7)

I_label = Label(data_frame, text="HSK63-PG10x100")
I_label.grid (row=4, column=6)
I = Entry(data_frame, width=17)
I.grid(row=4, column=7)

J_label = Label(data_frame, text="HSK63-PG10x120")
J_label.grid (row=5, column=6)
J = Entry(data_frame, width=17)
J.grid(row=5, column=7)

K_label = Label(data_frame, text="HSK63-PG15x100")
K_label.grid (row=6, column=6)
K = Entry(data_frame, width=17)
K.grid(row=6, column=7)

L_label = Label(data_frame, text="HSK63-PG15x120")
L_label.grid (row=7, column=6)
L = Entry(data_frame, width=17)
L.grid(row=7, column=7)

M_label = Label(data_frame, text="HSK63-PG15x160")
M_label.grid (row=8, column=6)
M = Entry(data_frame, width=17)
M.grid(row=8, column=7)

N_label = Label(data_frame, text="HSK63-PG25x100")
N_label.grid (row=9, column=6)
N = Entry(data_frame, width=17)
N.grid(row=9, column=7)

O_label = Label(data_frame, text="HSK63-PG32x100")
O_label.grid (row=10, column=6)
O = Entry(data_frame, width=17)
O.grid(row=10, column=7)

P_label = Label(data_frame, text="HSK63-SM075")
P_label.grid (row=11, column=6)
P = Entry(data_frame, width=17)
P.grid(row=11, column=7)

Q_label = Label(data_frame, text="HSK63-10SM2")
Q_label.grid (row=12, column=6)
Q = Entry(data_frame, width=17)
Q.grid(row=12, column=7)

R_label = Label(data_frame, text="HSK63-SM75-3.0")
R_label.grid (row=13, column=6)
R = Entry(data_frame, width=17)
R.grid(row=13, column=7)

# Remove Single Tool
def delete_tool():
    x = my_tree.selection()[0]
    my_tree.delete(x)
    conn = sqlite3.connect('data/tools.db')
    c = conn.cursor()
    
    c.execute("DELETE FROM tools WHERE oid=" + Seq.get())
    clear()
    
    conn.commit()
    conn.close()
    my_tree.delete(*my_tree.get_children())
    query_database()
# Remove Multiple Tool
def remove_many():
    response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")
    if response == 1:
        x = my_tree.selection()
        seqToDelete = []
        for record in x:
            seqToDelete.append(my_tree.item(record, 'values')[4])
        for record in x:
            my_tree.delete(record)
            
        conn = sqlite3.connect('data/tools.db')
        c = conn.cursor()
        c.executemany("DELETE FROM tools WHERE oid = ?", [(a,) for a in seqToDelete])
        
        seqToDelete = [] 
        conn.commit()
        conn.close()
        clear()
        my_tree.delete(*my_tree.get_children())
        query_database()
# Clear all entries
def clear():
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
    R.delete(0, END)
# Select Record
def select_record(e):
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
    R.delete(0, END)
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
# Update Tool
def update_tool():
    selected = my_tree.focus()
    my_tree.item(selected, text="", values=(Ignore.get(),
        SoflexRule.get(),
        MillRule.get(),
        DrillRule.get(),
        Seq.get(),
        Crib_FR.get(),
        Crib_AZ.get(),
        Type.get(),
        EssaiPartNumber.get(),
        EDPNum.get(),
        Description.get(),
        ThreadDescription11.get(),
        Diameter.get(),
        ShankDiameter.get(),
        ShoulderDiameter.get(),
        ShoulderLength.get(),
        ShoulderLenEnd.get(),
        ShoulderAngle.get(),
        MinOHL.get(),
        NumFlutes.get(),
        OAL.get(),
        LOC.get(),
        CornerRadius.get(),
        ThreadPitch.get(),
        ThreadClass.get(),
        TipAngle.get(),
        TipHeight.get(),
        TipDiameter.get(),
        ChamferLength.get(),
        Startshoulderlength.get(),
        ToolMaterial.get(),
        COATING.get(),
        Manufacturer.get(),
        NOTE.get(),
        AL.get(),
        S1.get(),
        CU.get(),
        PL.get(),
        PG.get(),
        ROUGH.get(),
        FIN.get(),
        ShapeName.get(),
        A.get(),
        B.get(),
        C.get(),
        D.get(),
        E.get(),
        F.get(),
        G.get(),
        H.get(),
        I.get(),
        J.get(),
        K.get(),
        L.get(),
        M.get(),
        N.get(),
        O.get(),
        P.get(),
        Q.get(),
        R.get(),))
    
    
    
    # Create or Connect to database
    conn = sqlite3.connect('data/tools.db')
    # DB Cursor
    c = conn.cursor()
    
    c.execute("""UPDATE tools SET
        Ignore = :Ignore,
        SoflexRule = :SoflexRule,
        MillRule = :MillRule,
        DrillRule = :DrillRule,
        Crib_FR = :Crib_FR,
        Crib_AZ = :Crib_AZ,
        Type = :Type,
        EssaiPartNum = :EssaiPartNum,
        EDPNum = :EDPNum,
        Description = :Description,
        ThreadDescription11 = :ThreadDescription11,
        Diameter = :Diameter,
        ShankDiameter = :ShankDiameter,
        ShoulderDiameter = :ShoulderDiameter,
        ShoulderLength = :ShoulderLength,
        ShoulderLenEnd = :ShoulderLenEnd,
        ShoulderAngle = :ShoulderAngle,
        MinOHL = :MinOHL,
        NumFlutes = :NumFlutes,
        OAL = :OAL,
        LOC = :LOC,
        CornerRadius = :CornerRadius,
        ThreadPitch = :ThreadPitch,
        ThreadClass = :ThreadClass,
        TipAngle = :TipAngle,
        TipHeight = :TipHeight,
        TipDiameter = :TipDiameter,
        ChamferLength = :ChamferLength,
        Startshoulderlength = :Startshoulderlength,
        ToolMaterial = :ToolMaterial,
        COATING = :COATING,
        Manufacturer = :Manufacturer,
        NOTE = :NOTE,
        AL = :AL,
        S1 = :S1,
        CU = :CU,
        PL = :PL,
        PG = :PG,
        ROUGH = :ROUGH,
        FIN = :FIN,
        ShapeName = :ShapeName,
        A = :A,
        B = :B,
        C = :C,
        D = :D,
        E = :E,
        F = :F,
        G = :G,
        H = :H,
        I = :I,
        J = :J,
        K = :K,
        L = :L,
        M = :M,
        N = :N,
        O = :O,
        P = :P,
        Q = :Q,
        R = :R
        
        WHERE oid = :oid""",
        {
            'Ignore':Ignore.get(),
            'SoflexRule':SoflexRule.get(),
            'MillRule':MillRule.get(),
            'DrillRule':DrillRule.get(),
            'Crib_FR':Crib_FR.get(),
            'Crib_AZ':Crib_AZ.get(),
            'Type':Type.get(),
            'EssaiPartNum':EssaiPartNumber.get(),
            'EDPNum':EDPNum.get(),
            'Description':Description.get(),
            'ThreadDescription11':ThreadDescription11.get(),
            'Diameter':Diameter.get(),
            'ShankDiameter':ShankDiameter.get(),
            'ShoulderDiameter':ShoulderDiameter.get(),
            'ShoulderLength':ShoulderLength.get(),
            'ShoulderLenEnd':ShoulderLenEnd.get(),
            'ShoulderAngle':ShoulderAngle.get(),
            'MinOHL':MinOHL.get(),
            'NumFlutes':NumFlutes.get(),
            'OAL':OAL.get(),
            'LOC':LOC.get(),
            'CornerRadius':CornerRadius.get(),
            'ThreadPitch':ThreadPitch.get(),
            'ThreadClass':ThreadClass.get(),
            'TipAngle':TipAngle.get(),
            'TipHeight':TipHeight.get(),
            'TipDiameter':TipDiameter.get(),
            'ChamferLength':ChamferLength.get(),
            'Startshoulderlength':Startshoulderlength.get(),
            'ToolMaterial':ToolMaterial.get(),
            'COATING':COATING.get(),
            'Manufacturer':Manufacturer.get(),
            'NOTE':NOTE.get(),
            'AL':AL.get(),
            'S1':S1.get(),
            'CU':CU.get(),
            'PL':PL.get(),
            'PG':PG.get(),
            'ROUGH':ROUGH.get(),
            'FIN':FIN.get(),
            'ShapeName':ShapeName.get(),
            'A':A.get(),
            'B':B.get(),
            'C':C.get(),
            'D':D.get(),
            'E':E.get(),
            'F':F.get(),
            'G':G.get(),
            'H':H.get(),
            'I':I.get(),
            'J':J.get(),
            'K':K.get(),
            'L':L.get(),
            'M':M.get(),
            'N':N.get(),
            'O':O.get(),
            'P':P.get(),
            'Q':Q.get(),
            'R':R.get(),
            'oid':Seq.get()
        })
 
    
    conn.commit()
    conn.close()
    
    
    
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
    R.delete(0, END)
# Add a new Tool
def add_tool():
    # create the database
        conn = sqlite3.connect('data/tools.db')
        # Create Cursor
        c = conn.cursor()

        #insert to table
        c.execute("INSERT INTO tools VALUES(:Ignore,:SoflexRule,:MillRule,:DrillRule, :Seq, :Crib_FR,:Crib_AZ,:Type,:EssaiPartNum,:EDPNum,:Description,:ThreadDescription11,:Diameter,:ShankDiameter,:ShoulderDiameter, :ShoulderLength, :ShoulderLenEnd, :ShoulderAngle, :MinOHL, :NumFlutes, :OAL, :LOC, :CornerRadius, :ThreadPitch, :ThreadClass, :TipAngle, :TipHeight, :TipDiameter, :ChamferLength, :Startshoulderlength, :ToolMaterial, :COATING, :Manufacturer, :NOTE, :AL, :S1, :CU, :PL, :PG, :ROUGH, :FIN, :ShapeName, :A, :B, :C, :D, :E, :F, :G, :H, :I, :J, :K, :L, :M, :N, :O, :P, :Q, :R)",
                {
                    'Ignore':Ignore.get(),
                    'SoflexRule':SoflexRule.get(),
                    'MillRule':MillRule.get(),
                    'DrillRule':DrillRule.get(),
                    'Seq':Seq.get(),
                    'Crib_FR':Crib_FR.get(),
                    'Crib_AZ':Crib_AZ.get(),
                    'Type':Type.get(),
                    'EssaiPartNum':EssaiPartNumber.get(),
                    'EDPNum':EDPNum.get(),
                    'Description':Description.get(),
                    'ThreadDescription11':ThreadDescription11.get(),
                    'Diameter':Diameter.get(),
                    'ShankDiameter':ShankDiameter.get(),
                    'ShoulderDiameter':ShoulderDiameter.get(),
                    'ShoulderLength':ShoulderLength.get(),
                    'ShoulderLenEnd':ShoulderLenEnd.get(),
                    'ShoulderAngle':ShoulderAngle.get(),
                    'MinOHL':MinOHL.get(),
                    'NumFlutes':NumFlutes.get(),
                    'OAL':OAL.get(),
                    'LOC':LOC.get(),
                    'CornerRadius':CornerRadius.get(),
                    'ThreadPitch':ThreadPitch.get(),
                    'ThreadClass':ThreadClass.get(),
                    'TipAngle':TipAngle.get(),
                    'TipHeight':TipHeight.get(),
                    'TipDiameter':TipDiameter.get(),
                    'ChamferLength':ChamferLength.get(),
                    'Startshoulderlength':Startshoulderlength.get(),
                    'ToolMaterial':ToolMaterial.get(),
                    'COATING':COATING.get(),
                    'Manufacturer':Manufacturer.get(),
                    'NOTE':NOTE.get(),
                    'AL':AL.get(),
                    'S1':S1.get(),
                    'CU':CU.get(),
                    'PL':PL.get(),
                    'PG':PG.get(),
                    'ROUGH':ROUGH.get(),
                    'FIN':FIN.get(),
                    'ShapeName':ShapeName.get(),
                    'A':A.get(),
                    'B':B.get(),
                    'C':C.get(),
                    'D':D.get(),
                    'E':E.get(),
                    'F':F.get(),
                    'G':G.get(),
                    'H':H.get(),
                    'I':I.get(),
                    'J':J.get(),
                    'K':K.get(),
                    'L':L.get(),
                    'M':M.get(),
                    'N':N.get(),
                    'O':O.get(),
                    'P':P.get(),
                    'Q':Q.get(),
                    'R':R.get(),
                    
                })

               
               
     

        # Commit Changes
        conn.commit()
        # Close connection
        conn.close()
        clear()
        # Update Treeview with new tools
        my_tree.delete(*my_tree.get_children())
        query_database()
    
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

add_button = Button(button_frame, text="Add Tool", command=add_tool)
add_button.grid(row=0, column=0, padx=10, pady=10)

update_button = Button(button_frame, text="Update Tool", command=update_tool)
update_button.grid(row=0, column=1, padx=10, pady=10)

delete_button = Button(button_frame, text="Remove Tool", command=delete_tool)
delete_button.grid(row=0, column=2, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Selected Tools", command=remove_many)
remove_many_button.grid(row=0, column=3, padx=10, pady=10)

select_button = Button(button_frame, text="Clear Form", command=clear)
select_button.grid(row=0, column=4, padx=10, pady=10)

# Add Menu
my_menu = Menu(root)
root.config(menu=my_menu)
#Import Menu
import_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Import/Export", menu=import_menu)
import_menu.add_command(label="Export Full BOM", command=export_bom)
import_menu.add_command(label="Export Short BOM", command=export_short_bom)
import_menu.add_separator()
import_menu.add_command(label="Import from Bom", command=BOM)

#Search Menu
search_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Search", menu=search_menu)
# Drop down menu
search_menu.add_command(label="Search", command=lookup_records)
search_menu.add_separator()
search_menu.add_command(label="Reset", command=query_database)

my_tree.bind("<ButtonRelease-1>", select_record)
# BOM() #run once!
query_database()

root.mainloop()
