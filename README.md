# Extracting supply chain maps from news articles using deep neural networks
Supplemental material for the paper "Extracting supply chain maps from news articles using deep neural networks" by Pascal Wichmann*, Alexandra Brintrup*, Simon Baker**, Philip Woodall*, and Duncan McFarlane* and submitted to the International Journal of Production Research (IJPR).

(*) = Institute for Manufacturing, University of Cambridge, United Kingdom

(**) = Language Technology Lab, University of Cambridge, United Kingdom

This paper is result of the PhD work by Pascal Wichmann.

## Paper abstract
Supply chains are increasingly global, complex and multi-tiered. Consequently, companies often struggle to maintain complete visibility of their supply network. This poses a problem as visibility of the network structure is required for tasks like effectively managing supply chain risk.

In this paper, we discuss automated supply chain mapping as a means of maintaining structural visibility of a company's supply chain, and we use Deep Learning to automatically extract buyer-supplier relations from natural language text.

Early results show that supply chain mapping solutions using Natural Language Processing and Deep Learning could enable companies to a) automatically generate rudimentary supply chain maps, b) verify existing supply chain maps, or c) augment existing maps with additional supplier information.

## Context

The paper and related work was done as part of my PhD at [DIAL](https://www.ifm.eng.cam.ac.uk/research/dial/), a research group at the [Institute for Manufacturing (IfM)](https://www.ifm.eng.cam.ac.uk) at the University of Cambridge.

The [repository for my PhD thesis](https://github.com/pwichmann/phd_thesis) provides some additional pointers and supplementary material.

## This repository

### Contents
This repository provides supplemental material, such as:
 * input samples (annotated sentences)
 * output samples (predicted relations between organisations)
 * a sample BiLSTM architecture.

### Limitations
For IP reasons, a pre-trained network, the full code or full training dataset cannot be generally provided.

### Academic access
You may request access to the training dataset or pre-trained model in the case of a legitimate desire to reproduce the presented academic results. In this case, you may not use the provided data for commercial purposes nor can you further redistribute the data.
Please create an issue with the subject "academic access", explain the motivation behind your request and specify the type of data you require. It is expected that you have a valid academic email address and have been working in a related field.

### Business interest
Please get in touch with [Versed AI](https://www.versed.ai) if you have a commercial interest in "mining" supply chain networks from large quantities of text. Versed AI is aiming to provide access to supply chain maps as a knowledge-as-a-service.
Since the publication of this paper, Versed AI's models have been trained on datasets significantly larger than the one described in this paper and are, thus, more accurate and robust than the initial prototype models.

### Input samples
100 random training samples are provided in a single *.json file.

The samples follow the basic structure shown by the following image:

<img src="https://github.com/pwichmann/supply_chain_mining/blob/master/img/sample_structure.png" width="500">

Explanation:

* ID is a unique ID of this particular arc. One sentence can result in many arcs as each pair of organisational named entities needs to be labelled.
* originalText is the unaltered original text; a text sequence automatically classified as a single sentence
* relations is a dictionary of the relations that require a label; each key corresponds to the unique id of such relation
* Since multiple annotators can have redundantly labelled a relation, the votes for different relation labels are stored. In this case, annotator "5ac41236..." has voted for label "2".
* x represents the feature vector and, thus, the sentence where organisational named entities have been masked. In this case, only two organisational named entities are present. The first one gets masked as \_\_NE\_FROM\_\_, the second gets masked at \_\_NE\_TO\_\_.
* y represents the response or target variable, in this case the assigned label "2". In case of multiple votes, a simple majority vote determines the winning label.

### Output samples

The output samples contain 200 randomly sampled predictions of the trained BiLSTM model.
The structure of the CSV file is as follows:

| Index | Masked sentence text | Original sentence text | Predicted label | Confidence score | ID of the predicted label |
|---|---|---|---|---|---|

The label definitions are as follows:

| Label ID | Relation |
|---|---|
| 0 | Reject = no relevant relation detected |
| 1 | B supplies A = the second-named organisation supplies the first-named |
| 2 | A supplies B = the first-named organisation supplies the second-named |
| 3 | Non-directed buyer-supplier relations; ambiguous relations; partnerships and collaborations  |
| 4 | Ownership relations; part-of relations |

## Versed AI
[Versed AI](https://www.versed.ai) is a new Cambridge University spin-out being formed by a post-doc and post-graduates from several different university departments. The team has developed Natural Language Processing (NLP) and Machine Learning (ML) technology for business intelligence purposes.

The technology can text-mine millions of news articles, business reports and social media for relationships between organisations, companies, products, and people. This information can be used to create vast knowledge networks that artificial intelligence is applied to in order to discover patterns and infer missing or unknown knowledge. These networks have many useful applications including predicting future relations and discovering information from the network structure. The first application the team intends to focus on is to automatically extract supply chain maps.

Among other achievements, the Versed AI team has won the Entrepreneurial Postdocs of Cambridge business plan competition (including a £20k investment sponsored by Cambridge Enterprise).

## License
The provided material is copyrighted and may not be used for commercial purposes.
