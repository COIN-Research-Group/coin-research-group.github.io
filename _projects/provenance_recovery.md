---
layout: page
title: Provenance Recovery
description: Uncovering the origins of the Sawhill Collection
img: assets/img/provenance_project/coin-matching.jpg
importance: 1
category: work
related_publications: false
---

Every coin has a history. Minted thousands of years ago these small objects where used in the everyday life of ancient persons. One day they were lost or buried only to be preserved by the Earth until found by future collectors. In modern times, sales of these coins have been preserved in auction catalogs that help us trace their *provenance* or history of ownership. This modern information completes the link between our ancient ancestors and the modern holder of any object.

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

Our latest work is available here:
- [Jackson Greer Presentation at CS Research Day](/blog/2025/jackson/)