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

# MODEL UPDATE

# Evaluation of Summary and Scores
## Text Provided:
MADISON, Wis.—Global Women’s Leadership Network (GWLN) Director Eleni Giakoumopoulos made her first ever presentation at an Asian credit union conference by leading sessions on empowering women to become leaders at September’s Asian Credit Union Forum 2024 in Bali, Indonesia. 

Asian Confederation of Credit Unions’ (ACCU) CEO Elenita San Roque, who has worked to expand the reach of GWLN Sister Societies to more than 20 Asian countries and received the 2016 Athena Leadership Award, invited Giakoumopoulos to give a September 7 main stage presentation that focused on strategies to close the gender gap and foster inclusive leadership within the credit union sector.  

Giakoumopoulos explored practical strategies for promoting gender diversity, inclusivity and equality within credit unions to empower women leaders, emphasizing that women must make their voice heard and seize leadership opportunities to tackle barriers and change the numbers for women in leadership.  

She encouraged male leaders to engage in women's empowerment efforts by opening conversations and providing opportunities for women to thrive. 

"We are doing this not just for us today but for the next generation—our daughters, granddaughters and their children," said Giakoumopoulos. “Women are an influential force in the global economy. In line with the mission of World Council to advance financial inclusion through the credit union and cooperative model, we are committed to championing economic empowerment for women through the Global Women's Leadership Network by consciously promoting gender equity and equality. It's smart for our countries, our credit unions and our communities when we invest in women.” 

Along with her main stage presentation, Giakoumopoulos also participated in a three-day Women’s Workshop held in the days leading up to the Forum.  

## Summary Provided:
### Summary:
Eleni Giakoumopoulos made her first presentation at an Asian credit union conference by leading sessions on empowering women to become leaders at September's Asian Credit Union Forum 2024 in Bali, Indonesia. She encourages male leaders to engage in women's empowerment efforts by opening conversations.

---

## Original Text Highlights:
### Event:
- **First-ever presentation** by Eleni Giakoumopoulos at the **Asian Credit Union Forum 2024**.
- Held in **Bali, Indonesia**.

### Topics Covered:
- **Empowering women** to become leaders in the credit union sector.
- **Engaging male leaders** in empowerment efforts through conversations and opportunities.

### Additional Points from the Original Text:
- Focused on **closing the gender gap** and fostering **inclusive leadership**.
- Participation in a **three-day Women’s Workshop** before the event.
- Emphasis on **economic empowerment** and **gender equality** as part of the Global Women's Leadership Network’s (GWLN) mission.

---

## Evaluation of the Provided Summary:

### Strengths:
- Captures the **essence of the event**, including Giakoumopoulos’s role and the **location (Bali)**.
- Reflects the core message of **empowering women** and **involving male leaders** in the conversation.

### Missing Details:
- Does not mention:
  - **Closing the gender gap** and fostering **inclusive leadership**.
  - Participation in the **three-day Women’s Workshop**.
  - Focus on **economic empowerment** through the Global Women’s Leadership Network (GWLN).
  - The **larger context** of investment in future generations and credit union benefits.

### Conclusion:
The summary captures the key points, but it could be more complete by including other aspects like the workshop, specific strategies discussed, and the focus on financial empowerment.

---

## Analysis of the Evaluation Scores

### ROUGE Scores:

- **ROUGE-1 (Unigram Overlap)**:
  - Precision: 0.91  
  - Recall: 0.64  
  - F1 Score: 0.75  
  **Interpretation**:  
  The generated summary captures most of the **key words** from the original text (high precision) but misses some relevant details (lower recall).

- **ROUGE-2 (Bigram Overlap)**:
  - Precision: 0.78  
  - Recall: 0.54  
  - F1 Score: 0.64  
  **Interpretation**:  
  The summary captures some **phrases (bigrams)** accurately, but it could include more relevant multi-word expressions to improve recall.

- **ROUGE-L (Longest Common Subsequence)**:
  - Precision: 0.88  
  - Recall: 0.62  
  - F1 Score: 0.73  
  **Interpretation**:  
  The summary maintains much of the **sequence and structure** of the original text, although some sections are omitted.

### BLEU Score:
- **Score**: 0.4050  
  **Interpretation**:  
  A BLEU score of **0.405** is fairly good, indicating that the **phrasing** in the generated summary matches the original text reasonably well, though there are some deviations.

### BERTScore:
- **Precision**: 0.9742  
- **Recall**: 0.9526  
- **F1 Score**: 0.9633  
  **Interpretation**:  
  **High BERTScore** values suggest that the **semantic meaning** of the generated summary aligns closely with the original text. This indicates that the summary accurately reflects the intent and ideas, even though it misses some specific details.

---

## Suggestions for Improvement:

### 1. Enhance Detail Coverage:
- Add details about the **three-day workshop** and the focus on **closing the gender gap**.
- Include the **economic empowerment message** and the emphasis on **future generations**.

### 2. Improve Recall:
- Incorporate more **multi-word phrases** from the original text to improve **ROUGE-2** and **ROUGE-L** scores.

### 3. Refine Phrasing:
- Slight rephrasing to match **specific expressions** from the original text could increase the **BLEU score**.

---

## Conclusion:

### Strengths:
- The generated summary captures the **key points** and aligns well with the **semantic meaning** of the original text (as shown by the **high BERTScore**).

### Weaknesses:
- The summary **omits several key details**, affecting **recall** in the ROUGE and BLEU scores.  
- These missing elements slightly reduce the overall **completeness**.

---

## Final Thoughts:
While the summary effectively communicates the **core ideas**, including additional relevant details would improve the **precision and recall**. This would ensure the summary aligns not just with the **meaning** but also with the **depth and structure** of the original content.

------------------------------------------------------------------------------------------------

# **Comparison of Results: First vs. Second Text**

---

## **1. ROUGE Scores Comparison**

| **Metric**         | **First Text** (F1) | **Second Text** (F1) |
|--------------------|---------------------|----------------------|
| **ROUGE-1**        | 0.39                | **0.75**             |
| **ROUGE-2**        | 0.18                | **0.64**             |
| **ROUGE-L**        | 0.28                | **0.73**             |

- **Conclusion:**  
  The **second text** significantly outperforms the first in all ROUGE metrics. It captures more unigrams, bigrams, and sequences of the original text, indicating better word, phrase, and structural alignment.

---

## **2. BLEU Score Comparison**

| **Metric** | **First Text** | **Second Text** |
|------------|----------------|-----------------|
| **BLEU**   | 0.0621         | **0.4050**      |

- **Conclusion:**  
  The **second text** achieves a much higher BLEU score, indicating better word sequence alignment with the reference text.

---

## **3. BERTScore Comparison**

| **Metric**  | **First Text** | **Second Text** |
|-------------|----------------|-----------------|
| **Precision** | 0.8849       | **0.9742**      |
| **Recall**    | 0.8880       | **0.9526**      |
| **F1**        | 0.8864       | **0.9633**      |

- **Conclusion:**  
  The **second text** has significantly higher BERTScore values, indicating better semantic alignment with the reference text.

---

## **Summary of Comparison**

| **Metric** | **Best Result** |
|------------|-----------------|
| **ROUGE-1** | Second Text     |
| **ROUGE-2** | Second Text     |
| **ROUGE-L** | Second Text     |
| **BLEU**    | Second Text     |
| **BERTScore** | Second Text   |

---

## **Final Verdict: Second Text is Better**

- **Second text** achieves **higher scores** across **all metrics**—ROUGE, BLEU, and BERTScore.  
- It demonstrates better **phrase alignment, word sequence matching, and semantic accuracy**.

### **Conclusion:**  
The **second text** is superior to the first in terms of both **quantitative metrics** and **semantic coherence**, making it the **better summary**.
