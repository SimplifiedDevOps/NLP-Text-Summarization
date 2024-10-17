# Text Summarization Using BART Transformer Model

## Project Overview
This project demonstrates text summarization using the **BART** (Bidirectional and Auto-Regressive Transformer) model. BART, a combination of **BERT** and **GPT**, is pre-trained on large datasets like CNN/DailyMail and can perform both **extractive** and **abstractive summarization**. The project involves two key stages:

1. **Without Fine-Tuning**: Using the pre-trained BART model for summarization without modifying its weights.
2. **With Fine-Tuning**: Adapting the BART model to a custom dataset (**DialogSum**) to improve the model’s performance on domain-specific tasks.

Performance evaluation is done using **ROUGE**, **BLEU**, and **BERTScore** metrics to assess how well the generated summaries align with reference summaries.

---

## Model Implementation Details

### Dataset Used:
- **DialogSum dataset**, containing dialogues and their corresponding summaries.
  - **Training Data**: 12,460 samples
  - **Testing Data**: 1,500 samples
  - **Validation Data**: 500 samples

### Implementation Steps:
1. **Stage 1**: Load the pre-trained BART model from Hugging Face.
2. **Stage 2**: Fine-tune the BART model on the DialogSum dataset.
3. **Stage 3**: Generate summaries for custom input texts (blogs or articles).
4. **Stage 4**: Evaluate performance using **ROUGE**, **BLEU**, and **BERTScore** metrics.

---

## Model Performance and Evaluation

### Sample Input Dialogue:
Between five and seven weeks, a pregnancy can be ended by a procedure called menstrual extraction. 
Another method is called the “morning after” pill, or emergency contraception. 
There are two types of emergency contraception:
One type is identical to ordinary birth control pills, anduses the hormones estrogen and progestin). This type is available with a prescription under the brand name Preven. But women can even use their regular birth control pills for emergency contraception, after they check with their doctor about the proper dose. About half of women who use birth control pills for emergency contraception get nauseated and 20 percent vomit. This method cuts the risk of pregnancy 75 percent. The other type of morning-after pill contains only one hormone: progestin, and is available under the brand name Plan B. It is more effective than the first type with a lower risk of nausea and vomiting. It reduces the risk of pregnancy 89 percent.

### Generated Summary:
There are two types of emergency contraception. One is identical to ordinary birth control pills and uses the hormones estrogen and progestin. 
The other contains only one hormone and is available under the brand name Plan B. 
It is more effective than the first type with a lower risk of nausea and vomiting.

## Evaluation Metrics

### 1. ROUGE Scores:
- **ROUGE-1 (Unigram Overlap)**:
  - Precision: 0.46  
  - Recall: 0.34  
  - F1 Score: 0.39  

- **ROUGE-2 (Bigram Overlap)**:
  - Precision: 0.21  
  - Recall: 0.15  
  - F1 Score: 0.18  

- **ROUGE-L (Longest Common Subsequence)**:
  - Precision: 0.33  
  - Recall: 0.25  
  - F1 Score: 0.28  

### 2. BLEU Score:
- **BLEU Score**: 0.0621  

### 3. BERTScore:
- Precision: 0.8849  
- Recall: 0.8880  
- F1 Score: 0.8864  

---

## Analysis of Results

### ROUGE Scores Analysis:
- **ROUGE-1** score of 0.39 shows that the summary captures some essential words from the reference but misses others.
- **ROUGE-2** score of 0.18 indicates limited overlap of bigrams, meaning the generated summary struggles to replicate phrases from the reference text.
- **ROUGE-L** score of 0.28 reflects some alignment with the sequence of ideas in the reference summary but suggests room for improvement.

### BLEU Score Analysis:
- The **BLEU score** of 0.0621 is low, indicating that the generated summary’s word sequences do not closely align with the reference summary.
- BLEU penalizes deviations in phrasing, emphasizing the differences in the structure between the generated and reference summaries.

### BERTScore Analysis:
- **High BERTScore** values (F1: 0.8864) show that the generated summary captures the **semantic meaning** well.
- Even if the wording differs, the summary aligns closely with the core ideas of the original text.

---

## Suggestions for Improvement

### 1. Enhance Phrase Matching:
- Fine-tune the model with more **epochs** to improve multi-word phrase matching and boost **ROUGE-2** and **BLEU** scores.

### 2. Experiment with Decoding Strategies:
- Increase **beam width** during generation to produce more coherent and aligned summaries.
- Use **length penalties** and **temperature sampling** to enhance fluency.

### 3. Use Data Augmentation:
- Incorporate additional **dialogue-based datasets** to help the model generalize across various dialogue styles.

### 4. Incorporate Post-Processing:
- Implement **post-processing techniques** to align the summary more closely with the input.

---

## Conclusion

### Strengths:
- **BERTScore** shows that the generated summaries retain the **core meaning** of the input text, even if the phrasing differs.
- The model demonstrates effectiveness at **abstractive summarization**, generating summaries with reasonable semantic accuracy.

### Weaknesses:
- **ROUGE** and **BLEU** scores indicate that the summaries struggle with **exact word and phrase alignment**, affecting precision.
- The model requires further **fine-tuning** to achieve better alignment with reference summaries.

---

## Final Thoughts
The **BART Transformer** model is effective for **abstractive summarization**, but further **fine-tuning** is needed to excel in structured summarization tasks. With improvements in **hyperparameters**, **decoding strategies**, and **training data**, the model can generate more precise and coherent summaries. This project successfully demonstrates the potential of **BART** for summarizing both **dialogues** and **custom text inputs**.
