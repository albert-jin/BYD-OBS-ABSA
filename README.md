# BYD-OBS-ABSA: Beyond Simple Observations, Embracing Comprehensive Contextual Insights for ABSA
Code Implementation about "Self-adaptive LLM instructions optimization for aspect-based sentiment analysis by incorporating emotion-oriented in-contexts"

## Overview

Aspect-Based Sentiment Analysis (ABSA) is a crucial task in natural language processing (NLP) that identifies sentiment towards specific entities or aspect terms within a text. Traditional deep learning-based ABSA methods often face challenges such as large domain-specific training data requirements and poor domain transferability. To address these issues, we propose the BYD-OBS-ABSA framework.

BYD-OBS-ABSA leverages unique in-context constraints, backgrounds, and analogical reasoning to address LLM hallucinations and enhance sentiment prediction accuracy. The framework integrates various in-context augmentation strategies, including emotion-oriented backgrounds, constraints, and analogical reasoning, further improving initial LLM instructions through adaptive iterative optimization using a random search bootstrap algorithm.

[![](/results/BYD-OBS-ABSA.png "Architecture of BYD-OBS-ABSA")][Architecture of BYD-OBS-ABSA]


## Key Features

- **Emotion-Oriented In-Context Constraints:** Constructs variant queries hypothesizing different polarities for aspect terms within a sentence, ensuring consistency and accuracy through a secondary evaluation mechanism.
- **In-Context Backgrounds:** Integrates aspect term background information into sentiment identification, enhancing the precision of sentiment analysis by leveraging LLM's ability to provide context-aware information.
- **In-Context Analogies:** Utilizes analogical reasoning to generate emotionally and contextually relevant examples, guiding the LLM in solving sentiment analysis tasks more effectively.
- **Self-Adaptive Bootstrap Instructions Optimization:** Enhances LLM predictions by iteratively refining prompts and examples, maximizing the benefits of LLM prompting.

## Performance

Extensive zero/few-shot experiments with GPT-3.5-turbo across six public datasets validate the effectiveness and robustness of BYD-OBS-ABSA, even surpassing human judgment in certain scenarios.

[![](/results/zero-shot.png "Zero Shot Performance of BYD-OBS-ABSA")][Zero Shot Performance of BYD-OBS-ABSA]

## Datasets

- **SemEval-2014:** Includes benchmarks for both the restaurant and laptop domains.
- **SemEval-2015:** Focuses on the restaurant domain.
- **SemEval-2016:** Covers the restaurant domain with diverse datasets.
- **Twitter:** Annotated tweets from the Twitter platform.
- **ACLShortData:** Social tweets annotated via Amazon Mechanical Turk.

## Comparison with Baselines

The BYD-OBS-ABSA framework demonstrates significant improvements over traditional and LLM-based baselines in zero-shot and few-shot settings. It systematically optimizes LLM instructions through emotion-oriented in-contexts and self-adaptive bootstrap instructions optimization, achieving higher accuracy in sentiment analysis tasks.

## Repository Structure

- **results**: Directory containing subdirectories for each dataset's results.
  - **ACLShort**
  - **laptop14**
  - **rest14**
  - **rest15**
  - **rest16**
  - **Twitter**
- **BasicSentAnalysis.ipynb**: Notebook for basic sentiment analysis.
- **BYD-ABSA.ipynb**: Main notebook for BYD-OBS-ABSA implementation.
- **BYD_Caul_Acc.ipynb**: Notebook for causal accuracy analysis.
- **Constraint.ipynb**: Notebook for constraint-based sentiment analysis.
- **DirectlyUGPT_ABSA.ipynb**: Notebook for direct usage of GPT for ABSA.
- **Incontext.ipynb**: Notebook for in-context learning experiments.
- **IntroSentAnalysis.ipynb**: Introductory sentiment analysis notebook.
- **Sentiment_Analysis.ipynb**: General sentiment analysis notebook.
- **Test.ipynb**: Notebook for testing various aspects of the implementation.
- **README.md**: This readme file.

## Getting Started

To run the BYD-OBS-ABSA framework, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/albert-jin/BYD-OBS-ABSA.git
   ```

2. Using these files at Google Colab or Python Jupyter Notebook.
   ```bash
   Run XXX.ipynb
   ```
   

