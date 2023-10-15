# On Device Translator 
## Introduction
The On Device Translator is designed to utilize ctranslate2 and transformers to provide translations between various languages. While the underlying model can support up to 200 languages, this project highlights the translation for a select group of languages through a web interface made possible by streamlit. We also use quantization technique so that we can use the model using cpu and its fast. 
## Dependencies
```
ctranslate2 
transformers 
streamlit
```
**Download the quantized NLLB model: [Model](https://drive.google.com/drive/folders/1aLlTZ40zyPRD8wTBC4OAu5momHCeI6-x?usp=sharing)**

## Working Principle of the On Device Translator 
The translator consists of two main components:
*Translation Engine (ctranslate2 and transformers): This performs the actual translation of the text.*
*Web Interface (streamlit): This provides a visual platform for users to input text, select a target language, and view the translated output.*

### Step-by-Step Process
User Input via Streamlit Interface:
A user accesses the web application and is presented with a text area to input the text they wish to translate.
A dropdown menu allows the user to select the target language.

### Tokenization:
Once the text is submitted, it undergoes tokenization via the transformers library. Tokenization converts the input text into tokens that machine translation models can understand.
Translation Preparation: The tokenized source text is prepared for translation. An additional prefix is added to the tokenized text, indicating the desired target language.

### Translation:
ctranslate2 takes the prepared tokens and translates them. The model used in this project is "nllb-200-distilled-600M", which can support various language pairs. For this application, a subset of those language pairs is used. The model produces tokenized target text as output.

### Detokenization:
The tokenized target text from the model is then converted back into a coherent string of text using the transformers library.

### Displaying the Translated Text:
The translated text is then displayed on the Streamlit interface, allowing the user to view the results.

### Underlying Model
The project uses the "nllb-200-distilled-600M" model from ctranslate2. This model is a distilled version trained on a large amount of bilingual data. The "nllb-200" suggests it's capable of supporting up to 200 languages. However, in this project, only a subset of these languages is made available for translation.

### Benefits of On-Device Translation
Privacy: Since the translations happen on the device (or server if hosted), user data is not sent to external servers, ensuring data privacy.
Speed: On-device translations can be faster as there's no need to communicate with external servers, eliminating potential latency.
