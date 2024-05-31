import pandas as pd

# read the excel file
df = pd.read_excel('week1.xlsx')

# list of emails to exclude
exclude_emails = ['mj', 'ashleigh', 'tija']

# filter out the excluded emails and select only the rows where the answer is correct, then sort by submission time
dataframe = df[(df['correct'] == "Yes") & (~df['email'].isin(exclude_emails))].sort_values(by='submitted_on')

# initialize a tracker for correct answers and a result list for the first 10 participants to reach 4 correct answers
tracker = {}
result = []

# loop through the dataframe
for index, row in dataframe.iterrows():
    email = row['email']
    
    # update the tracker for each participant
    if email in tracker:
        tracker[email] += 1
    else:
        tracker[email] = 1
    
    # check if the participant reached 5 correct answers
    if tracker[email] == 4:
        result.append(email)
        
        # stop if we have 10 participants
        if len(result) == 10:
            break

# print the result
print(result)
