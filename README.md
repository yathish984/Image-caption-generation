BDA Project Documentation — Image Caption Generator
1. Title

Image Caption Generator Using Deep Learning (BDA Project)

2. Abstract

The Image Caption Generator is a deep-learning-based application that automatically generates descriptive captions for uploaded images. The system uses a Transformer-based model (Vit-GPT2) that combines a Vision Encoder and a Text Decoder to understand image content and convert it into meaningful natural-language sentences.

This project demonstrates the integration of Machine Learning, NLP, and Web Technologies to build a complete full-stack AI application. The backend uses FastAPI with HuggingFace Transformers, and the frontend uses React for a smooth user interface.

3. Problem Statement

Humans can easily describe what they see, but computers cannot understand visual content without training. Traditional image classification only labels images but does not describe them.

Problem:
How can we design a system that automatically generates human-like captions from images with high accuracy?

4. Objectives

To build an AI system that extracts visual features from images

To implement a model that can convert image features into meaningful sentences

To develop a full-stack web application with FastAPI & React

To enable users to upload images and get captions instantly

To create a scalable, accurate, and user-friendly tool

5. Methodology
5.1 Steps

Data Input: User uploads an image

Image Preprocessing: Image converted to RGB and resized

Feature Extraction: Vision Transformer extracts features

Caption Generation: GPT2 Decoder generates meaningful text

Output: Caption displayed on UI

5.2 Model Used

🔥 nlpconnect/vit-gpt2-image-captioning

Encoder → ViT (Vision Transformer)

Decoder → GPT-2 (Language model)

Trained on Flickr8k, Flickr30k, COCO Captions

6. System Architecture
        ┌────────────────────────────┐
        │        Frontend (React)    │
        │  - Upload Image UI         │
        │  - Display Caption         │
        └──────────────┬────────────┘
                       │ POST /caption
        ┌──────────────▼────────────┐
        │     FastAPI Backend       │
        │ - Preprocess image        │
        │ - Load ML Model (ViT-GPT2)│
        │ - Generate caption        │
        └──────────────┬────────────┘
                       │ HuggingFace Model
        ┌──────────────▼────────────┐
        │   Vit-GPT2 Image Caption   │
        └────────────────────────────┘

7. Technologies Used
Component	Technology
Frontend	React.js, TailwindCSS
Backend	FastAPI, Uvicorn
ML Model	HuggingFace Transformers
Image Processing	Pillow (PIL)
Language	Python, JavaScript
Hosting (optional)	GitHub, Vercel, Render
8. Dataset Used

Model was pre-trained on:

Flickr8k

Flickr30k

MS COCO Dataset

Your project does not need dataset training — you use the pre-trained model.

9. Results / Output Screenshots (Add your real ones)
Upload Page
+------------------------------------+
|   [ Choose Image ]                 |
|                                    |
|   (preview)                        |
+------------------------------------+

Generated Caption
Caption: "A dog running across a grassy field."


You can add real screenshots from your frontend React UI.

10. Conclusion

The Image Caption Generator successfully demonstrates how deep learning models can interpret visual content and generate human-like descriptions. This project shows the powerful combination of Transformers, Vision AI, and Web Development to build intelligent applications.

The system can be extended in future by:

Adding multi-language captions

Training with custom datasets

Deploying on cloud platforms

Using BLIP-2, LLaVA, or GPT-4o-Vision for better accuracy

11. References

HuggingFace Transformers Documentation

ViT-GPT2 Image Captioning Model

FastAPI Documentation

MS COCO Dataset
