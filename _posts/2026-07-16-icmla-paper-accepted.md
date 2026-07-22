---
title: "Paper Accepted at ICMLA 2026: Metric Learning for Ancient Coin Identification"
date: 2026-07-16
layout: post
description: Our paper on using metric learning to match ancient coin images across auction catalogs has been accepted.
categories: ["publications", "machine learning"]
thumbnail: assets/img/coin-metric-learning/brutus-obv-hjb.jpg
images:
  lightbox2: false
  photoswipe: false
  spotlight: false
  venobox: false
published: false
---
<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/coin-metric-learning/adams-side-by-side.png" class="img-fluid rounded z-depth-1" zoomable=true %}
        <div class="caption">
            A stater of Velia as photographed for the 1972 sale of the President John Q. Adams and Descendants collection.
        </div>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/coin-metric-learning/sawhill-side-by-side.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
        <div class="caption">
            The same coin photographed again in 2023, decades later and under very different conditions.
        </div>
    </div>
</div>

We're happy to share that our paper, "Metric Learning for Ancient Coin Identification," has been accepted for publication at the [International Conference on Machine Learning and Applications (ICMLA 2026)](https://www.icmla-conference.org/icmla26/). The authors are Nathan Sprague (Professor of Computer Science), Jason Forsyth (Associate Professor of Engineering, Curator of Coins for the Madison Art Collection), Trevor Schonbrun (Engineering '27), Dhanshrée Atre (Computer Science '26), and Quinnie Lu (Engineering '29).

Establishing an ancient coin's provenance, its chain of prior ownership, usually means manually paging through decades of auction catalogs looking for a photograph of the same physical coin, and it's only done for coins deemed important enough to justify the effort. The Velia stater above is a case in point: matching its 1972 and 2023 photos took manual expert review, even though it's the exact same coin. Computer vision offers a natural fit: given a photo of a coin in hand, can a system search historical catalog imagery and surface earlier appearances of that exact specimen? 

Our approach borrows from face recognition, training an ArcFace-based embedding model so that images of the same coin land near each other in a learned feature space. A truncated ConvNeXt backbone extracts features from each coin photo, which the ArcFace loss then shapes into that space: same-coin images pulled close together, different coins pushed apart. Matching a new photo becomes a nearest-neighbor lookup against previously embedded catalog images, rather than a manual side-by-side comparison.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/coin-metric-learning/coin-resnet-embedding.svg" class="img-fluid rounded z-depth-1" %}
        <div class="caption">
            Fig. 1: A catalog photo is passed through the ConvNeXt/ArcFace backbone to produce an embedding, placing same-coin images near each other in the learned feature space.
        </div>
    </div>
</div>

To evaluate this fairly, we built a new dataset of 155 coins (154 photographed on both sides, plus one imaged only on the reverse) photographed under deliberately varied lighting and reproduction conditions, yielding 309 imaged coin sides and 3,708 images so that we could test the approach on realistic, controlled visual variation. Many of these coins are drawn from the [Sawhill Collection](https://www.flickr.com/photos/203809913@N03/albums/72177720330286039) at JMU, which we've already been photographing and cataloging as part of our broader provenance-recovery work, giving us a ready source of real coins with known identities to build the paired evaluation set around.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/coin-metric-learning/reproduction-variants-fig2.png" class="img-fluid rounded z-depth-1" zoomable=true %}
        <div class="caption">
            Fig. 2: Example outputs from the reproduction-variation pipeline for a single coin side. Note the significant lighting variations and reproduction artifacts.
        </div>
    </div>
</div>

Table I below summarizes our main result. Recall@k is the fraction of queries for which the correct matching coin appears somewhere in the top k retrieved results, and mAP (mean average precision) rewards ranking that correct match as close to the top as possible. Frozen off-the-shelf features (even strong ones like DINOv2) are far from sufficient for this instance-level matching task. Direct paired training is the strongest approach on this controlled proxy, which is expected since it trains on the same reproduction pipeline it is tested on. Our public-data ArcFace model, tuned using only the small paired set for augmentation selection, stays competitive with roughly a three-point gap, despite never seeing the paired examples as ordinary training data.

<div class="table-responsive rounded z-depth-1 mt-3 mb-3">
<table class="table table-bordered table-striped mb-0">
<caption class="caption-top text-center fw-bold py-2 mb-0">Table I. Retrieval results comparing the main training and representation regimes</caption>
<thead>
<tr><th>Method</th><th>Recall@1</th><th>Recall@5</th><th>Recall@10</th><th>mAP</th></tr>
</thead>
<tbody>
<tr><td>Frozen ConvNeXt features</td><td>15.63%</td><td>24.75%</td><td>30.18%</td><td>0.2824</td></tr>
<tr><td>DINOv2 (frozen features)</td><td>37.30%</td><td>52.42%</td><td>60.04%</td><td>0.5723</td></tr>
<tr><td>Direct paired ArcFace training</td><td>98.01%</td><td>99.30%</td><td>99.62%</td><td>0.9942</td></tr>
<tr class="table-warning"><td><strong>Public-data ArcFace, tuned aug. + trunc. + lighting</strong></td><td><strong>94.57%</strong></td><td><strong>97.66%</strong></td><td><strong>98.34%</strong></td><td><strong>0.9800</strong></td></tr>
</tbody>
</table>
</div>

Table II isolates the effect of each design choice by testing it separately: TPE-tuned augmentation, an added lighting augmentation, and truncating the ConvNeXt backbone to preserve more of its spatial feature map. TPE-tuned augmentation drives most of the gain, pushing a standard backbone from 49.92% to 76.97% Recall@1 by targeting the specific nuisance variation in Figure 2. Truncation adds a separate benefit, preserving spatial detail that lighting augmentation alone can't exploit. Lighting augmentation on its own has little effect, and even slightly hurts the tuned standard model. The tuned augmentation and truncation combine for our best result, which is why the main model in Table I uses both. (One truncated+lighting-only configuration is still being rerun after a checkpoint was lost, so that row is marked pending below.)

<div class="table-responsive rounded z-depth-1 mt-3 mb-3">
<table class="table table-bordered table-striped mb-0">
<caption class="caption-top text-center fw-bold py-2 mb-0">Table II. Ablation study for public-data ArcFace training</caption>
<thead>
<tr><th>Configuration</th><th>TPE Aug.</th><th>Lighting Aug.</th><th>Trunc.</th><th>R@1</th><th>R@5</th><th>R@10</th><th>mAP</th></tr>
</thead>
<tbody>
<tr><td>Standard ConvNeXt</td><td></td><td></td><td></td><td>49.92%</td><td>63.83%</td><td>69.81%</td><td>0.6767</td></tr>
<tr><td>Standard ConvNeXt + TPE-tuned aug.</td><td>✓</td><td></td><td></td><td>76.97%</td><td>85.83%</td><td>88.84%</td><td>0.8774</td></tr>
<tr><td>Standard ConvNeXt + lighting aug.</td><td></td><td>✓</td><td></td><td>50.00%</td><td>64.08%</td><td>69.84%</td><td>0.6762</td></tr>
<tr><td>Truncated ConvNeXt + manual aug.</td><td></td><td></td><td>✓</td><td>71.01%</td><td>82.24%</td><td>86.22%</td><td>0.8482</td></tr>
<tr><td>Standard ConvNeXt + TPE-tuned + lighting aug.</td><td>✓</td><td>✓</td><td></td><td>72.11%</td><td>81.56%</td><td>85.28%</td><td>0.8397</td></tr>
<tr><td>Truncated ConvNeXt + TPE-tuned aug.</td><td>✓</td><td></td><td>✓</td><td>94.17%</td><td>97.36%</td><td>98.29%</td><td>0.9782</td></tr>
<tr><td>Truncated ConvNeXt + lighting aug.</td><td></td><td>✓</td><td>✓</td><td colspan="4" style="text-align:center; font-style:italic;">rerun pending&mdash;checkpoint not preserved</td></tr>
<tr class="table-warning"><td><strong>Truncated ConvNeXt + TPE-tuned + lighting aug.</strong></td><td><strong>✓</strong></td><td><strong>✓</strong></td><td><strong>✓</strong></td><td><strong>94.57%</strong></td><td><strong>97.66%</strong></td><td><strong>98.34%</strong></td><td><strong>0.9800</strong></td></tr>
</tbody>
</table>
</div>

We'll post the full paper here once it's ready for public release, and we're excited to keep pushing this pipeline toward practical provenance recovery for the collection.
