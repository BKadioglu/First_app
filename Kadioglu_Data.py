import streamlit as st
import pandas as pd 
from pandas import read_excel
import os 




data = read_excel(r"C:\Users\berke\OneDrive\Masaüstü\Prices.xlsx")
data.dropna(subset=["KDGL QUOTE NO"],inplace = True)
data = data.astype(str)
data.reset_index(drop=True, inplace=True)
st.title("KADIOGLU AVIATION DATA LIST")
nav = st.sidebar.radio("",["Home","Search_by_year","Search_by_all"])
def search():
    if nav == "Search_by_year":
        x = 0
        part_no_text = st.sidebar.text_input("Enter the components part number:")
        years = st.slider("Filter data using years",2014,2021)
        if years == 2021:
            new_list = list()
            st.header("The components that quoted in 2021")
            for i in range (len(data)):
                if part_no_text == data["P/N"][i] and data["RFQ DATE"][i].startswith("2021") == True:
                    x += 1
                    st.header((str(x) + ")"))
                    st.table(data.loc[i])
                    new_list.append(i)
            if x >=1:
                st.success((str(x) + " component(s) have been found"))
                df_list = list()
                for i in range (len(new_list)):
                    x = data["SUPPLIER"][new_list[i]]
                    y = data["RECEIVED PRICE "][new_list[i]]
                    z = data["COND"][new_list[i]]
                    q = data["RFQ DATE"][new_list[i]][0:10]
                    w = [x,y,z,q]
                    df_list.append(w)
                col1,col2 = st.columns(2)
                df = pd.DataFrame(df_list,columns=["Supplier","Received Price","Condition","Date"])
                if col1.button("Comparison"):
                    st.table(df)
                    graph_list = list()
                    graph_sup_list = list()
                    
                    for i in range (len(df["Received Price"])):
                            graph_list.append(float(df["Received Price"][i]))
                            graph_sup_list.append(i)
                    graph = pd.DataFrame((tuple(graph_list)),graph_sup_list,columns=["Prices"])
                    st.bar_chart(graph)
                    col2.button("Close")
                elif col2.button("Close"):
                    st.write("")
                
            else:
                st.error("There is no component with that part number in this year")
        if years == 2020:
            new_list = list()
            st.header("The components that quoted in 2020")
            for i in range (len(data)):
                if part_no_text == data["P/N"][i] and data["RFQ DATE"][i].startswith("2020") == True:
                    x += 1
                    st.header((str(x) + ")"))
                    st.table(data.loc[i])
                    new_list.append(i)
            if x >=1:
                st.success((str(x) + " component(s) have been found"))
                df_list = list()
                for i in range (len(new_list)):
                    x = data["SUPPLIER"][new_list[i]]
                    y = data["RECEIVED PRICE "][new_list[i]]
                    z = data["COND"][new_list[i]]
                    q = data["RFQ DATE"][new_list[i]][0:10]
                    w = [x,y,z,q]
                    df_list.append(w)
                col1,col2 = st.columns(2)
                df = pd.DataFrame(df_list,columns=["Supplier","Received Price","Condition","Date"])
                if col1.button("Comparison"):
                    st.table(df)
                    graph_list = list()
                    graph_sup_list = list()
                    
                    for i in range (len(df["Received Price"])):
                            graph_list.append(float(df["Received Price"][i]))
                            graph_sup_list.append(i)
                    graph = pd.DataFrame(tuple(graph_list),graph_sup_list,columns=["Prices"])
                    st.bar_chart(graph)
                    col2.button("Close")
                elif col2.button("Close"):
                    st.write("")
                
            else:
                st.error("There is no component with that part number in this year")
        if years == 2019:
            new_list = list()
            st.header("The components that quoted in 2019")
            for i in range (len(data)):
                if part_no_text == data["P/N"][i] and data["RFQ DATE"][i].startswith("2019") == True:
                    x += 1
                    st.header((str(x) + ")"))
                    st.table(data.loc[i])
                    new_list.append(i)
            if x >=1:
                st.success((str(x) + " component(s) have been found"))
                df_list = list()
                for i in range (len(new_list)):
                    x = data["SUPPLIER"][new_list[i]]
                    y = data["RECEIVED PRICE "][new_list[i]]
                    z = data["COND"][new_list[i]]
                    q = data["RFQ DATE"][new_list[i]][0:10]
                    w = [x,y,z,q]
                    df_list.append(w)
                col1,col2 = st.columns(2)
                df = pd.DataFrame(df_list,columns=["Supplier","Received Price","Condition","Date"])
                if col1.button("Comparison"):
                    st.table(df)
                    graph_list = list()
                    graph_sup_list = list()
                    
                    for i in range (len(df["Received Price"])):
                            graph_list.append(float(df["Received Price"][i]))
                            graph_sup_list.append(i)
                    graph = pd.DataFrame(tuple(graph_list),graph_sup_list,columns=["Prices"])
                    st.bar_chart(graph)
                    col2.button("Close")
                elif col2.button("Close"):
                    st.write("")
                
            else:
                st.error("There is no component with that part number in this year")
        if years == 2018:
            new_list = list()
            st.header("The components that quoted in 2018")
            for i in range (len(data)):
                if part_no_text == data["P/N"][i] and data["RFQ DATE"][i].startswith("2018") == True:
                    x += 1
                    st.header((str(x) + ")"))
                    st.table(data.loc[i])
                    new_list.append(i)
            if x >=1:
                st.success((str(x) + " component(s) have been found"))
                df_list = list()
                for i in range (len(new_list)):
                    x = data["SUPPLIER"][new_list[i]]
                    y = data["RECEIVED PRICE "][new_list[i]]
                    z = data["COND"][new_list[i]]
                    q = data["RFQ DATE"][new_list[i]][0:10]
                    w = [x,y,z,q]
                    df_list.append(w)
                col1,col2 = st.columns(2)
                df = pd.DataFrame(df_list,columns=["Supplier","Received Price","Condition","Date"])
                if col1.button("Comparison"):
                    st.table(df)
                    graph_list = list()
                    graph_sup_list = list()
                    
                    for i in range (len(df["Received Price"])):
                            graph_list.append(float(df["Received Price"][i]))
                            graph_sup_list.append(i)
                    graph = pd.DataFrame(tuple(graph_list),graph_sup_list,columns=["Prices"])
                    st.bar_chart(graph)
                    col2.button("Close")
                elif col2.button("Close"):
                    st.write("")
                
            else:
                st.error("There is no component with that part number in this year")
        if years == 2017:
            new_list = list()
            st.header("The components that quoted in 2017")
            for i in range (len(data)):
                if part_no_text == data["P/N"][i] and data["RFQ DATE"][i].startswith("2017") == True:
                    x += 1
                    st.header((str(x) + ")"))
                    st.table(data.loc[i])
                    new_list.append(i)
            if x >=1:
                st.success((str(x) + " component(s) have been found"))
                df_list = list()
                for i in range (len(new_list)):
                    x = data["SUPPLIER"][new_list[i]]
                    y = data["RECEIVED PRICE "][new_list[i]]
                    z = data["COND"][new_list[i]]
                    q = data["RFQ DATE"][new_list[i]][0:10]
                    w = [x,y,z,q]
                    df_list.append(w)
                col1,col2 = st.columns(2)
                df = pd.DataFrame(df_list,columns=["Supplier","Received Price","Condition","Date"])
                if col1.button("Comparison"):
                    st.table(df)
                    graph_list = list()
                    graph_sup_list = list()
                    
                    for i in range (len(df["Received Price"])):
                            graph_list.append(float(df["Received Price"][i]))
                            graph_sup_list.append(i)
                    graph = pd.DataFrame(tuple(graph_list),graph_sup_list,columns=["Prices"])
                    st.bar_chart(graph)
                    col2.button("Close")
                elif col2.button("Close"):
                    st.write("")
                
            else:
                st.error("There is no component with that part number in this year")
        if years == 2016:
            new_list = list()
            st.header("The components that quoted in 2016")
            for i in range (len(data)):
                if part_no_text == data["P/N"][i] and data["RFQ DATE"][i].startswith("2016") == True:
                    x += 1
                    st.header((str(x) + ")"))
                    st.table(data.loc[i])
                    new_list.append(i)
            if x >=1:
                st.success((str(x) + " component(s) have been found"))
                df_list = list()
                for i in range (len(new_list)):
                    x = data["SUPPLIER"][new_list[i]]
                    y = data["RECEIVED PRICE "][new_list[i]]
                    z = data["COND"][new_list[i]]
                    q = data["RFQ DATE"][new_list[i]][0:10]
                    w = [x,y,z,q]
                    df_list.append(w)
                col1,col2 = st.columns(2)
                df = pd.DataFrame(df_list,columns=["Supplier","Received Price","Condition","Date"])
                if col1.button("Comparison"):
                    st.table(df)
                    graph_list = list()
                    graph_sup_list = list()
                    
                    for i in range (len(df["Received Price"])):
                            graph_list.append(float(df["Received Price"][i]))
                            graph_sup_list.append(i)
                    graph = pd.DataFrame(tuple(graph_list),graph_sup_list,columns=["Prices"])
                    st.bar_chart(graph)
                    col2.button("Close")
                elif col2.button("Close"):
                    st.write("")
                
            else:
                st.error("There is no component with that part number in this year")
        if years == 2015:
            new_list = list()
            st.header("The components that quoted in 2015")
            for i in range (len(data)):
                if part_no_text == data["P/N"][i] and data["RFQ DATE"][i].startswith("2015") == True:
                    x += 1
                    st.header((str(x) + ")"))
                    st.table(data.loc[i])
                    new_list.append(i)
            if x >=1:
                st.success((str(x) + " component(s) have been found"))
                df_list = list()
                for i in range (len(new_list)):
                    x = data["SUPPLIER"][new_list[i]]
                    y = data["RECEIVED PRICE "][new_list[i]]
                    z = data["COND"][new_list[i]]
                    q = data["RFQ DATE"][new_list[i]][0:10]
                    w = [x,y,z,q]
                    df_list.append(w)
                col1,col2 = st.columns(2)
                df = pd.DataFrame(df_list,columns=["Supplier","Received Price","Condition","Date"])
                if col1.button("Comparison"):
                    st.table(df)
                    graph_list = list()
                    graph_sup_list = list()
                    
                    for i in range (len(df["Received Price"])):
                            graph_list.append(float(df["Received Price"][i]))
                            graph_sup_list.append(i)
                    graph = pd.DataFrame(tuple(graph_list),graph_sup_list,columns=["Prices"])
                    st.bar_chart(graph)
                    col2.button("Close")
                elif col2.button("Close"):
                    st.write("")
                
            else:
                st.error("There is no component with that part number in this year")
        if years == 2014:
            new_list = list()
            st.header("The components that quoted in 2014")
            for i in range (len(data)):
                if part_no_text == data["P/N"][i] and data["RFQ DATE"][i].startswith("2014") == True:
                    x += 1
                    st.header((str(x) + ")"))
                    st.table(data.loc[i])
                    new_list.append(i)
            if x >=1:
                st.success((str(x) + " component(s) have been found"))
                df_list = list()
                for i in range (len(new_list)):
                    x = data["SUPPLIER"][new_list[i]]
                    y = data["RECEIVED PRICE "][new_list[i]]
                    z = data["COND"][new_list[i]]
                    q = data["RFQ DATE"][new_list[i]][0:10]
                    w = [x,y,z,q]
                    df_list.append(w)
                col1,col2 = st.columns(2)
                df = pd.DataFrame(df_list,columns=["Supplier","Received Price","Condition","Date"])
                if col1.button("Comparison"):
                    st.table(df)
                    graph_list = list()
                    graph_sup_list = list()
                    
                    for i in range (len(df["Received Price"])):
                            graph_list.append(float(df["Received Price"][i]))
                            graph_sup_list.append(i)
                    graph = pd.DataFrame(tuple(graph_list),graph_sup_list,columns=["Prices"])
                    st.bar_chart(graph)
                    col2.button("Close")
                elif col2.button("Close"):
                    st.write("")
                
            else:
                st.error("There is no component with that part number in this year")      
    if nav == "Search_by_all":
         x = 0
         part_no_text = st.sidebar.text_input("Enter the components part number:")
         new_list = list()
         st.header("The components that quoted between 2014-2021")
         for i in range (len(data)):
                if part_no_text == data["P/N"][i]:
                    x += 1
                    st.header((str(x) + ")"))
                    st.table(data.loc[i])
                    new_list.append(i)
         if x >=1:
                st.success((str(x) + " component(s) have been found"))
                df_list = list()
                for i in range (len(new_list)):
                    x = data["SUPPLIER"][new_list[i]]
                    y = data["RECEIVED PRICE "][new_list[i]]
                    z = data["COND"][new_list[i]]
                    q = data["RFQ DATE"][new_list[i]][0:10]
                    w = [x,y,z,q]
                    df_list.append(w)
                col1,col2 = st.columns(2)
                df = pd.DataFrame(df_list,columns=["Supplier","Received Price","Condition","Date"])
                if col1.button("Comparison"):
                    st.table(df)
                    graph_list = list()
                    graph_sup_list = list()
                    for i in range (len(df["Received Price"])):
                            graph_list.append(float(df["Received Price"][i]))
                            graph_sup_list.append((i))
                    graph = pd.DataFrame(tuple(graph_list),graph_sup_list,columns=["Prices"])
                    st.bar_chart(graph)
                    col2.button("Close")
                elif col2.button("Close"):
                    st.write("")
                
         else:
                st.error("There is no component with that part number in this year")      
        
search()


             