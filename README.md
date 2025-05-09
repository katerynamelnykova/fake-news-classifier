# Fake News Detection System
A system for detecting fake news using machine learning techniques. Developed as part of a bachelor's thesis in information systems and technologies.


## 📂 Project Structure

The project contains several Jupyter notebooks, each covering a specific part of the pipeline:

- `data_cleaning_isot.ipynb` — performs cleaning and preprocessing of the **ISOT Fake News Dataset**
- `classical_models.ipynb` — applies classical machine learning methods:
  - Logistic Regression
  - Random Forest
  - Naive Bayes (Multinomial)
  - Support Vector Machine (SVM)
- `neural_networks_isot.ipynb` — applies neural network architectures:
  - GRU (Gated Recurrent Unit)
  - LSTM (Long Short-Term Memory)
  - Bi-LSTM (Bidirectional LSTM)

## 🌐 Web Application

A web interface is built using **FastAPI**. It allows users to interact with the system by entering their news text and analyzing whether it is fake or real. Users can also **select which model** will be used for the analysis.

### 🔌 Backend

The app runs at:  
**http://127.0.0.1:8000**

Interactive documentation is available at:  
**http://127.0.0.1:8000/docs**

---

### 📨 Example request body

```json
{
  "text": "Donald Trump just couldn t wish all Americans a Happy New Year and leave it at that. Instead, he had to give a shout out to his enemies, haters and  the very dishonest fake news media.  The former reality show star had just one job to do and he couldn t do it. As our Country rapidly grows stronger and smarter, I want to wish all of my friends, supporters, enemies, haters, and even the very dishonest Fake News Media, a Happy and Healthy New Year,  President Angry Pants tweeted.  2018 will be a great year for America! As our Country rapidly grows stronger and smarter, I want to wish all of my friends, supporters, enemies, haters, and even the very dishonest Fake News Media, a Happy and Healthy New Year. 2018 will be a great year for America!  Donald J. Trump (@realDonaldTrump) December 31, 2017Trump s tweet went down about as welll as you d expect.What kind of president sends a New Year s greeting like this despicable, petty, infantile gibberish? Only Trump! His lack of decency won t even allow him to rise above the gutter long enough to wish the American citizens a happy new year!  Bishop Talbert Swan (@TalbertSwan) December 31, 2017no one likes you  Calvin (@calvinstowell) December 31, 2017Your impeachment would make 2018 a great year for America, but I ll also accept regaining control of Congress.  Miranda Yaver (@mirandayaver) December 31, 2017Do you hear yourself talk? When you have to include that many people that hate you you have to wonder? Why do the they all hate me?  Alan Sandoval (@AlanSandoval13) December 31, 2017Who uses the word Haters in a New Years wish??  Marlene (@marlene399) December 31, 2017You can t just say happy new year?  Koren pollitt (@Korencarpenter) December 31, 2017Here s Trump s New Year s Eve tweet from 2016.Happy New Year to all, including to my many enemies and those who have fought me and lost so badly they just don t know what to do. Love!  Donald J. Trump (@realDonaldTrump) December 31, 2016This is nothing new for Trump. He s been doing this for years.Trump has directed messages to his  enemies  and  haters  for New Year s, Easter, Thanksgiving, and the anniversary of 9/11. pic.twitter.com/4FPAe2KypA  Daniel Dale (@ddale8) December 31, 2017Trump s holiday tweets are clearly not presidential.How long did he work at Hallmark before becoming President?  Steven Goodine (@SGoodine) December 31, 2017He s always been like this . . . the only difference is that in the last few years, his filter has been breaking down.  Roy Schulze (@thbthttt) December 31, 2017Who, apart from a teenager uses the term haters?  Wendy (@WendyWhistles) December 31, 2017he s a fucking 5 year old  Who Knows (@rainyday80) December 31, 2017So, to all the people who voted for this a hole thinking he would change once he got into power, you were wrong! 70-year-old men don t change and now he s a year older.Photo by Andrew Burton/Getty Images.",
  "model": "svc_linear_kernel"
}
```

### Available models

- `logistic_regression`
- `svc_linear_kernel`
- `random_forest`
- `naive_bayes`
- `bi_lstm`
- `lstm`
- `gru`

---

## 🚀 How to Run

Python 3.12 is required to run this project locally without Docker.

A `Makefile` is provided to simplify installation and launching.

### 🔧 Show all available commands

```bash
make help
```

### 🛠️ Install all dependencies

```bash
make install
```

Installs the required packages listed in `requirements.txt`.

### ▶️ Run the FastAPI app

```bash
make run
```

Runs the FastAPI server with `uvicorn`.

### 🔄 Install and run in one step

```bash
make install_and_run
```

---

### 🐳 Run with Docker (no need to install Python locally)

If you prefer containerized execution, you can build and run the app using Docker:

#### 🔨 Build the Docker image

```bash
docker build -t fake-news-app .
```

#### ▶️ Run the app in a container

```bash
docker run -it --rm -p 8000:8000 fake-news-app
```

