import pickle

import prob as prob

statement = input("Enter the news that you want to predict")
print("you entered" + str(statement))


def news(var):
    load_model = pickle.load(open('model.sav', 'rb'))
    prediction = load_model.predict([statement])
    return (print("The given statement is ", prediction[0])),


if __name__ == '__main__':
    news(var)
