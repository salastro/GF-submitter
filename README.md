# *G*oogle *F*orms submitter
***THIS IS FOR EDUCATIONAL PURPOSES ONLY, DON'T TRY RUNNING SOMEONE'S ELSE FORMS
USING THIS***

## Inspiration

This was made in response to pointless school projects in which you need a
certain amount of data to discuss some kind of topic. Sometimes, the data itself
is not the important part, rather it is the discussion. Thus, sufficient data to
progress the discussion is needed.

## User-friendliness

User-friendliness was not a priority since this is a "garbage" script made to
solve a quick affectless problem for convenience purposes. You have to scrap
your way using this script; it is a more of a guide than a usable tool.

## Usage

1. Put the link of the google form you want to use in the `link` variable
   (`https://docs.google.com/forms/d/e/{form-id}/viewform`).
2. Submit the form with recognizable data entries while capturing the network
   with inspect tools, select formResponse and then payload tab, click view
   source and copy the text into `entries` variable.
3. *(optional)* Recognize the entered data and format the text to use random
   data using `random.choices` and `faker.Faker` according to your needs.
4. Change the value of the in the loop to the number of responses you want.
5. Run the script
6. ...
7. **Profit**
