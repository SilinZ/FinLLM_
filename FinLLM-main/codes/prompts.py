#%%
prompt_1 = """Your task is to carefully read an earnings call transcript and extract the most important facts that may influence the stock price for the next trading day. You should find out as many independent facts as possible. Additionally, note the sentiment of the company speakers (e.g., optimism, caution, concern) and include it as one of the facts.

### Instructions:
1. **Understand the Context**:
   - Identify the company's current financial performance, focusing on metrics like revenue, net income, earnings per share (EPS), and margins.
   - Look for any forward-looking statements, guidance updates, or outlooks provided by the management.
   - Pay attention to the tone and sentiment of the company speakers, capturing whether they express optimism, caution, or concern.

2. **Extract Key Facts**:
   - Highlight critical announcements such as product launches, partnerships, acquisitions, or divestitures.
   - Note any surprising or significant statements, such as exceeding or missing market expectations (e.g., EPS beats, revenue misses).
   - Pay attention to comments on macroeconomic trends or external factors affecting the company (e.g., interest rates, supply chain issues).

3. **Identify Market-Relevant Insights**:
   - Distill facts that the market is likely to react to, such as:
     - Surprises in earnings or guidance.
     - Innovations, new market entries, or expansion plans.
     - Management tone or sentiment shifts (e.g., optimism, caution).

### Response Format:

1. [State the fact clearly, including relevant numbers or details.]
2. [State another fact.]
3. [more facts]
......
n. [Include the sentiment of the company speakers, with specific examples where possible.]


Remember to only provide your response in the specified format, including facts and sentiment. Do not provide any additional commentary or analysis.

Here is the earnings call transcript for your analysis:"""

#%%
prompt_2 = """
### Task: Analyze and Predict Next-Day Stock Price Movement

You are tasked with analyzing key facts extracted from an earnings call transcript to predict the company's stock price movement for the next trading day. Your goal is to evaluate each fact and predict its potential impact using **if-then-because** statements. These statements should reflect how the fact may influence the stock price and provide clear reasoning based on near-term market behavior and sentiment.

---

### **Response Format**:
If [summarize the fact], then [how it would affect the next day stock price], because [the rationale behind it, considering near-term market behavior and sentiment].
If [summarize the fact], then [how it would affect the next day stock price], because [the rationale behind it, considering near-term market behavior and sentiment].
If [summarize the fact], then [how it would affect the next day stock price], because [the rationale behind it, considering near-term market behavior and sentiment].
...

---

### **Important Guidelines**:
1. **Focus on the Short-Term**: Your analysis should focus specifically on **next trading day** stock price movement.
2. **Consider Market Reactions**:
   - Account for surprises, forward guidance, sentiment, and sector-specific trends.
   - Reflect on investor expectations and how they align with the facts.
3. **Rely on Market Behavior and Sentiment**:
   - Use near-term behavior such as momentum effects or emotional reactions to surprises as part of your rationale.
4. **Abstraction of Facts**:
   - Where appropriate, generalize or abstract facts to make the analysis more effective and insightful.
5. **Strict Adherence to the Format**:
   - Only provide **if-then-because** statements.
   - Do not include additional commentary, analysis, or explanations outside the specified format.

---

### Input:
Here are the extracted facts for your analysis:  
"""

#%%
prompt_3 = """
### Task: Predict the Next Day Stock Price Movement

You are a financial analyst AI tasked with predicting the next day's stock price movement for a company based on information from its most recent earnings call. You will be provided with the following inputs:

1. **Facts**: Key information extracted from the company's earnings call transcript. These facts include:
   - Financial performance metrics (e.g., revenue growth, EPS, margins).
   - Product announcements, guidance updates, and other relevant data.

2. **If-Then-Because Statements**: Statements that describe how next-day stock price movements have historically been influenced by similar facts. These statements have been accumulated from prior earnings calls and are provided as a reference. Past statements may also be useful.

---

### **Your Task**:
1. **Identify Relevant Facts and Statements**:
   - Determine which facts and statements are most relevant for predicting the next day's stock price movement.
   - Focus on the key drivers of market reaction (e.g., surprises, forward guidance, or sentiment).

2. **Analyze the Relevant Information**:
   - Analyze how the selected facts align with the relevant if-then-because statements.
   - Provide a concise explanation of how the facts and statements together influence your prediction.

3. **Predict the Next Day’s Stock Price Movement**:
   - Choose one of the following categories for your prediction:
     - **Positive Surprise** (+3% or more): A strong positive market reaction.
     - **Moderate Positive** (+1% to +3%): A modest positive market reaction.
     - **Flat Response** (-1% to +1%): Little to no significant market reaction.
     - **Moderate Negative** (-1% to -3%): A modest negative market reaction.
     - **Negative Surprise** (-3% or more): A strong negative market reaction.

---

### **Response Format**:
Analysis: Provide an analysis explaining how the facts and selected statements drive your prediction. Focus on the key factors and rationale.

Statements Used: List the numbers of the statements you used in your analysis.

Prediction: Choose one of the five categories.

---

### **Input Example**:

**Facts**:
- Alphabet Inc. reported Q3 2024 revenue growth of 15% year-over-year to $76.5 billion for Google Services and 35% growth in Google Cloud revenues, reaching $11.4 billion, with a 17% operating margin.
- Alphabet's consolidated net income increased 34% to $26.3 billion, with earnings per share rising 37% to $2.12, alongside operating margin expansion to 32%.
- Alphabet plans to invest heavily in AI infrastructure, maintaining Q4 CapEx at Q3's $13 billion level, primarily for servers and data centers, with further increases expected in 2025.

**Statements**:
1. If Alphabet reported Q3 2024 revenue growth of 15% for Google Services and 35% for Google Cloud with strong operating margins, then the stock price is likely to increase, because these metrics suggest robust financial performance, exceeding market expectations, and highlight Alphabet's growing dominance in high-margin cloud services.
2. If Alphabet's consolidated net income grew 34% to $26.3 billion and EPS rose 37%, with operating margins expanding to 32%, then the stock price is likely to increase, because these financial metrics exceed expectations and demonstrate effective cost management, boosting investor sentiment.
3. If Alphabet plans to invest heavily in AI infrastructure, maintaining $13 billion in CapEx for Q4 and increasing in 2025, then the stock price could face slight pressure, because while such investments signal long-term growth, short-term investors may worry about increased expenses impacting near-term profitability.

---

### **Output Example**:
Analysis: Alphabet's Q3 earnings reflect robust financial performance, with strong revenue growth in Google Services and Cloud and significant EPS increases. These factors suggest positive market sentiment. However, heavy AI infrastructure investments and management's warnings of tougher year-over-year comparisons may temper investor enthusiasm. While the long-term growth prospects are strong, the market may focus on near-term profitability concerns, leading to mixed reactions.

Statements Used: 1, 2

Prediction: Flat Response (-1% to +1%)

---

### **Instructions**:
1. Focus on identifying and analyzing the most relevant facts and statements.
2. Base your analysis and prediction on short-term market reactions (next trading day).
3. Use the provided response format strictly, without adding unnecessary commentary or deviating from the task.

Here are the facts and statements for your analysis:  
"""

#%%
prompt_4 = """### **Prompt for Evaluating Statements**

You are an AI tasked with analyzing the usefulness and correctness of **if-then-because** statements for predicting the next day’s stock price movement. Your primary goal is to evaluate how well these statements contribute to the next day price prediction task and to recommend refinements or eliminations for statements that are not useful or accurate for this specific purpose.

---

### **Inputs**:
1. **Prediction Results**:  
   - The correctness of the previous stock price prediction based on five categories:  

2. **Facts Used**:  
   - The facts from the earnings call transcript that were used in the prediction.  

3. **Statements Used**:  
   - The **if-then-because** statements that were referenced in the prediction.  

4. **Actual Stock Movement**:  
   - The observed stock price movement category after the earnings call.  

---

### **Your Task**:
1. **Overall Analysis**:  
   - Assess the correctness of the expert’s prediction compared to the actual stock movement.  
   - Analyze the factors that contributed to the prediction's correctness or incorrectness, such as whether the facts and statements used were relevant and aligned with market behavior. If the input text didn't give sufficient information, use your own financial expertise. 

2. **Evaluate Each Statement**:  
   For each **if-then-because** statement, perform the following:  
   - Rate its **Relevance for Next-Day Prediction**: High/Medium/Low.  
   - Rate its **Rationale Consistency**: Consistent/Inconsistent.  
   - Provide a brief explanation of how this statement impacted the prediction’s correctness or incorrectness.  

3. **Suggest Improvements or Eliminations**:  
   - Refine statements that require improvement in their expected outcomes or rationale.  
   - Eliminate statements that are irrelevant or inaccurate for next-day predictions.  

---

### **Response Format**:  

**Overall Analysis**:  
- [Summary of how correct/incorrect the prediction was and key factors influencing its accuracy.]

**Analysis of Statements**:  
1. [Restate the statement]  
   - Relevance for Next-Day Prediction: [High/Medium/Low]  
   - Rationale Consistency: [Consistent/Inconsistent]  
   - Notes: [Brief explanation of why the statement is or isn’t effective for next-day price predictions.]  

2. [Restate the statement]  
   - Relevance for Next-Day Prediction: [High/Medium/Low]  
   - Rationale Consistency: [Consistent/Inconsistent]  
   - Notes: [Brief explanation.]

...

**Suggestions**:  
- **Statements to Refine**:  
  - [ID and refined version of statements that need improvement.]  
- **Statements to Eliminate**:  
  - [ID of the statements that are no longer useful.]

---

### **Example Input**:  

**Prediction Results**: Moderate Positive (+1% to +3%)  
**Facts Used**:  
- **Fact 1**: Alphabet's revenue grew by 15% YoY, with Google Cloud growing by 35%.  
- **Fact 2**: Operating margins increased to 32%.  
- **Fact 3**: Alphabet announced a significant increase in AI-related capital expenditures.  

**Statements Used**:  
1. If a company's revenue grows significantly and beats expectations, then the stock price is likely to rise because strong revenue performance signals robust business health and growth potential.  
2. If operating margins improve, then the stock price is likely to rise because higher margins indicate improved profitability and operational efficiency.  
3. If a company announces a significant increase in capital expenditures, then the stock price is likely to fall because high CapEx raises concerns about near-term profitability.  

**Actual Stock Movement**: Flat Response (-1% to +1%)

---

### **Example Output**:  

**Overall Analysis**:  
The expert's prediction of "Moderate Positive" was slightly incorrect, as the actual stock movement was a "Flat Response." While revenue and operating margin improvements supported a positive outlook, the market appeared more cautious due to increased capital expenditures. The CapEx statement assumed a negative reaction but overlooked the strategic nature of these investments, which balanced market sentiment.

---

**Analysis of Statements**:  
1. If a company's revenue grows significantly and beats expectations, then the stock price is likely to rise because strong revenue performance signals robust business health and growth potential.  
   - Relevance for Next-Day Prediction: High  
   - Rationale Consistency: Consistent  
   - Notes: This statement aligned with the facts but overestimated the positive impact, as the market likely priced in the revenue growth beforehand.  

2. If operating margins improve, then the stock price is likely to rise because higher margins indicate improved profitability and operational efficiency.  
   - Relevance for Next-Day Prediction: High  
   - Rationale Consistency: Consistent  
   - Notes: This statement correctly identified profitability improvements but did not fully account for other balancing factors like CapEx.  

3. If a company announces a significant increase in capital expenditures, then the stock price is likely to fall because high CapEx raises concerns about near-term profitability.  
   - Relevance for Next-Day Prediction: Low  
   - Rationale Consistency: Inconsistent  
   - Notes: The market viewed CapEx investments as strategic, contributing to balanced sentiment rather than a decline.

---

**Suggestions**:  
- **Statements to Refine**:  
  - Original: 1. If a company's revenue grows significantly and beats expectations, then the stock price is likely to rise because strong revenue performance signals robust business health and growth potential.  
    Refined: 1. If a company's revenue grows significantly but aligns with expectations, then the stock price is likely to remain flat because the positive performance may already be priced in.  

- **Statements to Eliminate**:  
  - 3. If a company announces a significant increase in capital expenditures, then the stock price is likely to fall because high CapEx raises concerns about near-term profitability.  
  
**Notes**: 
- Remember to give your responses strictly in the format. Especially, remember to always give the number of a statement when making suggestions about refinement or elimination for better tracking. 
- As a financial analyst, you should be picky about the statements used since not all statements used were useful, that is, even if the prediction was only slightly incorrect or correct, you can still refine or eliminated statements as many as you want.

Here are the input:  
"""