# cell-segmentation
Contains source code, datasets, related proofs and reports related to my cell segmentation research project

The following is a README for the cell-cell interface concavity algorithm I designed. I list all files in the directory and their functions below:

**Concavity Measure 3D.ipynb**: A .ipynb notebook containing the main algorithm and its related utilities. Explanations for each section of the algorithm + its utilities are included alongside the code in text blocks and inline comments.

**visualize_3d.py**: A .py file for visualizing algorithm behavior for specified borders in MayaVi. Will ask for a key, and requires zipfile output from the MayaVi Output section of Concavity Measure 3D.ipynb in the cwd. See that file for more details -- example output folders are included in this folder as well.

**visualize_ambrose.py**: A .py file for visualizing the final segmented output on the Ambrose slice. Requires the 'ambrose' zipfile output in the cwd -- this is already generated and in the folder. Can be regenerated via the MayaVi Output in Concavity Measure 3D.ipynb.


**Concavity Presentation.pdf**: The Google Slides presentation I gave to the group in pdf format. Provides an introductory overview to the project, in case reminders are necessary.

**graphmerge1_correctness.pdf**: A pdf of a proof of correctness for the graph merge algorithm used in the concavity merging stage. See Concavity Measure 3D.ipynb for the algorithm -- may be useful to look at while examining the proof. 

**ambrose** [folder]: The zipfile output for Ambrose, generated via the MayaVi Output section of Concavity Measure 3D.ipynb. Example input for visualize_ambrose.py -- also present in Concavity Presentation.pdf

**["i j"]** [folder]: the zipfile output for the border between segment ID i and segment ID j, generated via the Output section of Concavity Measure 3D.ipynb. Example inputs for visualize_3d.py -- when prompted for a key, supply the name of a folder to visualize its contents. Includes examples belonging to each histogram peak + present in Concavity Presentation.pdf: ("428 429", "628 750", "897 944")


I also include useful items for each of these dataset: (The numbers correspond to the original dataset "chunk_cell_[num].tif".)
- ambrose
- 0213 
- 0160
- 0184
- 0206

For each of the above datasets, I include the following:

- **[name].mat**: The oversegmented watershed dataset that feeds into Concavity Algorithm 3D.ipynb.

- **[name]_widths.txt**: The calculated widths of each cell in the given dataset. Output of a block of Concavity Measure 3D.ipynb that takes hours to complete -- reading these in via the next block skips this downtime. See Concavity Measure 3D.ipynb for more details.



**README.md**: This file.