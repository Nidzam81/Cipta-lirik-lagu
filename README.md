# Cipta-lirik-lagu

This project purpose is to train my LTSM model to create Malay song lyric. 
For deployment I'm using python Dash framework.  
 
## Training sample 
For training, I compiled 96 malay song lyrics into Lirik lagu 
.txt file. 
 
## Algorithm 
I trained the model using 1 layer bidirectional LTSM and 2 layer bidirectional LTSM and saved the model 
 
## Deplyoment 
I used python Dash to deploy the models. It will automatically display available h5 files and allow us 
to select which model to used. By inputing the seed word into "Perkataan benih" and selecting the lenght 
of the word that we want to predict into the "Panjang perkataan" field, when we push "Cipta" button, it will 
generate predicted lyrics. 

Below video shows how the app works 

[![SC2 Video](https://img.youtube.com/vi/dC40-aIf6LA/0.jpg)](http://www.youtube.com/watch?v=dC40-aIf6LA) 

## Future improvement 
Because we're just training around 96 song lyrics, I don't think it will be good enough. I do think if we add more 
song lyrics, the model can improve more. 
