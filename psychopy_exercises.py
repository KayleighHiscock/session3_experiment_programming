# These are some homework exercises to practice working 
#  with pandas and psychopy.

## Exercise A
# 1. Load pandas and psychopy
import pandas as pd 
import psychopy as ps 
from psychopy import visual, core, sound  

# 2. Load the picture verification simuli file
#    (look up the .read_csv method of pandas)
# picture_df = pd.read_csv('picture_verification_stimuli.csv')
    
# print(picture_df)

# 3. Loop over the item names, and print them on the screen
#    (you can loop over a single column just like a list!)
#print(picture_df['item'])

# for item in picture_df['item']:
#     print(item)
    
# 4. Now, change your code to show a text stimulus with each item name,
#     with a 1 second pause in between, instead of using print().
       
#window = visual.Window(size=(400, 400))
#for item in picture_df['item']:
    #text_stim = visual.TextStim(window, text=item)
    #text_stim.draw()
    #window.flip()
    #core.wait(1.0)

# 5. Loop over the item paths, and use them to create image stimuli;
#     display each image for 1 second.

# window = visual.Window(size=(400, 400))
# for item in range(0, len(picture_df)):
#     picture = picture_df.loc[item, 'image_file']
#     image = visual.ImageStim(window, image=picture)
#     image.draw()
#     window.flip()
#     core.wait(1.0)



## Exercise B
# 1. Load the lexical decision stimuli file 
lexical_df = pd.read_csv('lexical_decision_stimuli.csv')
#print(lexical_df)

# 2. Select all the high frequency words (HF)
#    (you can do this using masks, just like how we selected a single row)
frequency = 'HF'
mask = lexical_df['freq_category'] == frequency #returns boolean values 
hf_words = lexical_df[mask]['word']
print(hf_words)


# 3. Loop over the words, and create a sound stimulus for each
#    (you can specify the relative path as f'sounds/HF/{sound_name}.wav')

window = visual.Window(size=(400, 400))

true_values_df = hf_words
for i in len(true_values_df):
    each_word = true_values_df.iloc[i]
    audio = sound.Sound(f'sounds/HF/{each_word}.wav')
    audio.play()
    window.flip()
    core.wait(1.0)

# 4. Play the sounds one-by-one, making sure there is some time between them




## Bonus exercise
# 1. Try to load in the image and/or sound stimuli first, 
#     before showing/playing them. You can use a list, and the .append()
#     method, to build a list of stimuli, and then use another for loop
#     to show/play them one by one.
# 2. Before showing/playing, try to randomise the order of stimuli; 
#     Google how to randomise the order of a list! (hint: shuffle!)
