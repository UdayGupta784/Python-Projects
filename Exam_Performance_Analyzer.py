import pandas as pd

df = pd.read_csv("student_scores.csv",index_col="id")

#Calculation of Avg. Score For Each Student
df["Average Score"] = df[["Science","English","History","Maths"]].mean(axis=1)

#Giving Rank To each students based on Overall Performmance
df["Overall Rank"] = df["Average Score"].rank( ascending=False,method="dense").astype(int)
#Assigning Grades To Each Student
def grade(avg):
    if avg>=90:
        return "O"
    elif avg<90 and avg>=75:
        return "A"
    elif  avg<75 and avg>=65:
        return "B"
    elif  avg<65 and avg>=55:
        return "C"
    elif  avg<55 and avg>=45:
        return "D"
    elif  avg<45 and avg>=35:
        return "E"
    else:
        return "F"

df["Grade"] = df["Average Score"].apply(grade)

#Function To Get a Filtered result for user
def get_result(df,section = "ALL",gender="BOTH",G="ALL"):
    temp = df.copy()
    if section != "ALL":
        temp = temp[temp["Section"]==section]
    if gender != "BOTH":
        temp = temp[temp["Gender"].str.upper()==gender]
    if G != "ALL":
        temp = temp[temp["Grade"]==G]
    temp = temp.sort_values(by=["Average Score","Age"],ascending = [False,True])
    temp["Filter Rank"] = range(1,len(temp)+1)
    return temp

#User Input
S = input("Enter The Section: ").strip().upper()
Gen = input("Enter The Gender Of Student: ").strip().upper()
Gra = input("Enter Grade Of Students: ").strip().upper()
result = get_result(df,S,Gen,Gra)
#Saving Required Result To A Txt File:
if result.empty:
    print("No Records Found For Apllied Filter")
else:
    with open("Exam_Performance.txt",'w') as f:
        f.write(f"Result For Section- {S},Gender- {Gen},Gra- {Gra}\n")
        f.write(f"Number Of Students- {len(result)}\n")
        f.write(result.to_string())
        f.write("\n---------------------------------------------------------------------------------------------------------------------------------")
        print("Your Result Is Saved In Exam_Performance.txt")