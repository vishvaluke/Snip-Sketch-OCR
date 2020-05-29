<h1 id="what-is-snip-&-sketch-ocr">What is Snip &amp; Sketch OCR?</h1>
<ul>
<li>Snip and Sketch OCR is a python based tool that lets user to snip an image or content and extract all the acceptable characters from it.</li>
<li>Snip &amp; Sketch OCR incorporates both Snip &amp; Sketch(Microsoft) and Tesseract OCR (Google) functionalities to allow users retrieve certain information from virtually any kind of content without downloading the whole file.</li>
<li>Snip &amp; Sketch OCR also uses Image Processing(OpenCV) to help the user achieve better Tesseract OCR results.</li>
</ul>
<h1 id="types-of-snip--sketch-ocr">Types of Snip &amp; Sketch OCR:</h1>
<ol>
<li>Better Results &amp; GUI:<br>
Better image optimizing algorithm and wxPython GUI to deliver functionality such as copy and save content. Resulting in a time delay in extraction of acceptable characters.</li>
<li>Faster Execution :<br>
Simple image optimizing algorithm, bash based output deliver window and only show and copy to clipboard functionality. Being a multi threaded program it executes at faster pace.</li>
</ol>
<p><strong>To Get better Execution speed use <a href="https://www.pypy.org/">pypy</a> compiler instead of python’s built in compiler.</strong></p>
<p><strong>To make it more user friendly and easily accessible use <a href="autohotkey.com/">autohotkey</a> and compile the short_ssocr.ahk and add the short_ssocr.ahk to Task scheduler(Windows) for automatic start up.</strong></p>
<h1 id="run-the-script">Run the Script</h1>
<ol>
<li>Download <a href="https://sourceforge.net/projects/tesseract-ocr/">Tesseract_OCR</a> and extract it to current Snip &amp; Sketch OCR directory and check for all the requirements.</li>
<li>Run the desired python script.</li>
<li>Snip the content.</li>
<li>Based on selected python script you will prompted with GUI or bash interfaces.</li>
</ol>
<p><strong>Disclaimer:</strong> In Better Results and GUI python script all the extracted content will always be saved in same notepad (copied.txt).</p>
