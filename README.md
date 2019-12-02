# Extracting supply chain maps from news articles using deep neural networks
Supplemental material for the paper "Extracting supply chain maps from news articles using deep neural networks" by Pascal Wichmann*, Alexandra Brintrup*, Simon Baker**, Philip Woodall*, and Duncan McFarlane* and submitted to the International Journal of Production Research (IJPR).

(*) = Institute for Manufacturing, University of Cambridge, United Kingdom

(**) = Language Technology Lab, University of Cambridge, United Kingdom

This paper is result of the PhD work by Pascal Wichmann.

## Paper abstract
Supply chains are increasingly global, complex and multi-tiered. Consequently, companies often struggle to maintain complete visibility of their supply network. This poses a problem as visibility of the network structure is required for tasks like effectively managing supply chain risk. 

In this paper, we discuss automated supply chain mapping as a means of maintaining structural visibility of a company's supply chain, and we use Deep Learning to automatically extract buyer-supplier relations from natural language text. 

Early results show that supply chain mapping solutions using Natural Language Processing and Deep Learning could enable companies to a) automatically generate rudimentary supply chain maps, b) verify existing supply chain maps, or c) augment existing maps with additional supplier information.

## This repository
This repository provides supplemental material, such as:
 * input samples (annotated sentences)
 * output samples (predicted relations between organisations)
 * a sample BiLSTM architecture.
 
A pre-trained network, the full code or full training dataset cannot be provided for IP reasons.

Please get in touch with [Versed AI](https://www.versed.ai) if you would like to get access for academic purposes or have a business interest. 

### Input samples
100 random training samples are provided in a single *.json file.

The structure of each sample is shown by the following image:



## Versed AI
[Versed AI](https://www.versed.ai) is a new Cambridge University spin-out being formed by a post-doc and post-graduates from several different university departments. The team has developed Natural Language Processing (NLP) and Machine Learning (ML) technology for business intelligence purposes.

The technology can text-mine millions of news articles, business reports and social media for relationships between organisations, companies, products, and people. This information can be used to create vast knowledge networks that artificial intelligence is applied to in order to discover patterns and infer missing or unknown knowledge. These networks have many useful applications including predicting future relations and discovering information from the network structure. The first application the team intends to focus on is to automatically extract supply chain maps.

Among other achievements, the Versed AI team has recently won the Entrepreneurial Postdocs of Cambridge business plan competition (including a £20k investment sponsored by Cambridge Enterprise).
