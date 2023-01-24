import streamlit as st
import numpy as np
import pandas as pd
import streamlit as st
import pickle


model = pickle.load(open("dectree.pkl", "rb"))


st.title("Bipolar Disorder Phase Prediction")
st.write("For each question rank the best score that describes how much you have been bothered by each problem during the past 2 Weeks")
x1=st.number_input("Age")
x0=st.number_input("Gender: 0-Male,1-Female")
x2=st.slider("Interest in doing things or work?",0,3)
x3=st.slider("Feeling Depressed or Hopeless?",0,3)
x4=st.slider("Feeling irritated or angry than usual?",0,3)
x5=st.slider("Sleeping less than usual but have a lot of energy?",0,3)
x6=st.slider("Doing more risky things than usual?",0,3)
x7=st.slider("Feeling nervous,worried or on edge?",0,3)
x8=st.slider("Feeling panic or frightened?",0,3)
x9=st.slider("Avoiding situations that makes you anxious",0,3)
x10=st.slider("Feeling that your illness is not taken seriously enough?",0,3)
x11=st.slider("Thoughts of actually hurting yourself?",0,3)
x12=st.slider("Problems with your sleep that affects your overall sleep quality",0,3)
x13=st.slider("Problems with memory?",0,3)
x14=st.slider("Unpleasant thoughts or images that repeatedly enter your mind?",0,3)
x15=st.slider("Not feeling close to other people?",0,3)
y1=st.slider("Feeling alone?",0,4)
y2=st.slider("Feeling stressed?",0,4)
y3=st.slider("could not stop feeling sad?",0,4)
y4=st.slider("wanted to be by myself?",0,4)
y5=st.slider("It was hard for me to have fun",0,4)
y6=st.slider("How easily you are annoyed by others?",0,2)
y7=st.slider("How often you lose your temper?",0,2)
y8=st.slider("Get angry frequently",0,2)
y9=st.slider("Lose temper easily",0,2)
y10=st.slider("Overall irritability causes me problems",0,2)
y11=st.slider("How often you feel more self confident than usual,rate it",1,5)
y12=st.slider("How often you need less sleep than usual? rate it",1,5)
y13=st.slider("How often do yoy talk with new people than usual? rate it",1,5)
st.write("If you have been bothered by thoughts that kept coming into your mind that you would do something bad or that something bad would happen to you or someone else")
y15=st.slider("How much time is occupied by these thoughts or behaviors each day?",1,5)
y16=st.slider("How much do they bother you?",1,5)
y17=st.slider("How hard is it for you to control them?",1,5)
y18=st.slider("How much do they interfere with school, your social or family life, or your job?",1,5)
y19=st.slider("How restless was your sleep?",1,5)
y20=st.slider("How satisfied were you with your sleep?",1,5)
y21=st.slider("How refreshing was your sleep?",1,5)
y22=st.slider("Do you have difficulty in falling asleep? rate it",1,5)
y23=st.slider("Rate your sleep quality",1,5)
st.write("During the past 7 days, how much have you been bothered by any of the following problems?")
y25=st.slider("Stomach pain",0,2)
y26=st.slider("Back pain",0,2)
y27=st.slider("Pain in your arms,legs or joints",0,2)
y28=st.slider("Have you ever felt like something awful will happen?",1,5)
y29=st.slider("Do you feel worried about the future",1,5)
y30=st.slider("Do you feel nervous",1,5)
y31=st.slider("Do you get scared easily?",1,5)
y32=st.slider("Are you worried when you are away from home?",1,5)

def predicts(x1,x0,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y15,y16,y17,y18,y19,y20,y21,y22,y23,y25,y26,y27,y28,y29,y30,y31,y32):
    pred=model.predict([[x1,x0,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y15,y16,y17,y18,y19,y20,y21,y22,y23,y25,y26,y27,y28,y29,y30,y31,y32]])
    print(pred)
    return pred




def main():
    btn=st.button("predict")
    st.write("RESULT")
    if btn:
        result=predicts(x1,x0,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y15,y16,y17,y18,y19,y20,y21,y22,y23,y25,y26,y27,y28,y29,y30,y31,y32)
        if result==3:
            st.write("You have no symptoms of Bipolar")
        elif result==2:
            st.write("Mania:Your level of Stress,Anxiety and sleeping problems are high")
            st.write("Please consult Doctor as soon as possilble.")
        elif result==1:
            st.write("Hypomania:You have mild problems and symptoms.")
            st.write("Please consult doctor")
        elif result==0:
            st.write("Depression:You have the least symptoms.Take care of your mental health")
            

if __name__=='__main__':
    main()

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
