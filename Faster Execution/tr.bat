# Set Correct directory of Snip & Sketch OCR 
@ECHO OFF
cd /d d:
cd /"Snip & Sketch OCR"
echo %cd%
python cpocr.py
PAUSE
