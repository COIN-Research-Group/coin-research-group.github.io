---
layout: page
title: Provenance Recovery
description: Uncovering the origins of the Sawhill Collection
img: assets/img/provenance_project/coin-matching.jpg
importance: 1
category: work
related_publications: false
---

Every coin has a history. Minted thousands of years ago, these small objects were used in the everyday life of ancient persons. One day they were lost or buried, only to be preserved by the Earth until found by future collectors. In modern times, sales of these coins have been preserved in auction catalogs that help us trace their *provenance* or history of ownership. This modern information completes the link between our ancient ancestors and the modern holder of any object.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/provenance_project/sawhill-catalogs.jpg" class="img-fluid rounded z-depth-1"  zoomable=true %}
        <div class="caption">
            Sawhill's catalogs at present in the Madison Art Collection
        </div>
    </div>
    
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/provenance_project/resnet-50.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
        <div class="caption">
            ResNet-50 model
        </div>
    </div>
    
</div>


While we know Dr. Sawhill began his collection in the 1930s, we have little information about where he purchased his coins. However, we do have his personal auction catalogs, correspondence with dealers, and purchase invoices. Our current project seeks to recover this lost provenance information by comparing his personal auction catalogs to high-resolution scans of the existing collection. We utilize deep learning methods with custom loss functions to tune models towards the individual differences between unique coins.

---

## Research Approach

Our core task is coin re-identification: given a high-resolution scan of a coin from the Sawhill collection, can we match it to the same coin as it appeared in an auction catalog photograph from decades earlier? This is a fundamentally challenging problem — the images differ in lighting, angle, resolution, and age — and it cannot be solved with standard classification techniques because we are matching objects across two domains without labeled pairs.

We approach this using **deep metric learning**, which trains a neural network to embed images into a vector space where visually similar coins are close together and dissimilar coins are far apart. We use architectures such as ResNet-50 as backbones and experiment with custom loss functions (e.g., triplet loss, contrastive loss) tuned toward the subtle surface differences that distinguish individual ancient coins from one another.

---

## Student Research

Our undergraduate researchers have made significant contributions to this project, presenting their work at regional and national conferences.

### Jackson Greer — Deep Metric Learning Baseline (2024–25)

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/cs_day_2025/jackson-cs.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
        <div class="caption">
            Jackson Greer presenting at JMU CS Research Day, Spring 2025
        </div>
    </div>
</div>

Jackson Greer (CS '25) established the baseline deep metric learning framework for coin identification and provenance recovery. He applied multiple metric learning methods to existing datasets of Roman Republican coins and validated the approach using sample images from the Sawhill collection. His work demonstrated the feasibility of cross-domain coin matching and set the foundation for subsequent research.

Presentation: [Coin Identification with Deep Metric Learning (PDF)](/assets/pdf/greer-deep-metric-learning.pdf)

---

### Trevor Schonbrun — Augmentation Tuning & Explainability (2025–26)

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/ay25-26-presentations/trevor-ai.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
        <div class="caption">
            Trevor Schonbrun presenting at the VASEM/VirginiaAI Conference, September 2025
        </div>
    </div>
</div>

Trevor Schonbrun presented at the [Virginia Academy of Science, Engineering, and Medicine — AI Summit](https://www.vabio.org/event/vasem-virginiaai-charting-the-future-of-ai-in-virginia/) (September 30–October 1, 2025, Virginia Tech Institute for Advanced Computing, Arlington, VA). His work focused on systematically tuning data augmentation strategies to improve model robustness to the visual variation between catalog and collection images, and on developing explainable AI visualizations to interpret what features the network relies on when matching coins.

Presentation: [Augmentation Tuning Poster (PDF)](/assets/pdf/trevor-ai-summit-poster.pdf)

---

### Dhanshrée Aire — Automated Data Collection & Alternative Backbones (2025–26)

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/ay25-26-presentations/shree-capwic.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
        <div class="caption">
            Dhanshrée Aire presenting at the CAPWIC Conference, March 2026
        </div>
    </div>
</div>

Dhanshrée Aire presented at the [ACM Capital Area Women in Computing (CAPWIC)](https://capwic.org/) conference (March 27–28, 2026). Her research examined methods for automating the data collection pipeline — reducing the manual effort required to build training datasets from auction catalog scans — and experimentally compared alternative computer vision backbones to determine which architectures best capture the fine-grained visual features needed for accurate coin re-identification.

Presentation: [CAPWIC Poster (PDF)](/assets/pdf/shree-capwic-poster.pdf)

---

## News & Updates

- [Trevor Schonbrun and Dhanshrée Aire Student Presentations](/blog/2026/student-presentations/)
- [Jackson Greer Presentation at CS Research Day](/blog/2025/jackson/)