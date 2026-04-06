# CISC-121-FINAL-PROJECT

https://github.com/user-attachments/assets/b9d38d29-4cf9-42bd-8562-9fc5274d8202

Welcome to Horse Analyzer 3000

# Project description:

This project is a Python application made to analyze the three possible values that Minecraft gives when spawning a horse: Speed, Health and Jump height.
This application allows the user to sort horses by their best attribute using a Bubble Sort algorithm and determine which one is the best.

# Computational Thinking :

The problem was broken down into smaller steps

- Collect horse data from Minecraft
- Extract speed, jump, and health values
- Store horses in a list
- Sort the horses based on a selected attribute
- Display the best horse

# Abstraction

The goal was to create a application to substitute the entire minecraft build to test each horse for each attribute. 
The program focuses only on numerical values (speed, jump, health) to simplify the problem. It gets the value from the command F3-i which copies a /summon command
It goes through the whole string and than takes it values, stores in a list and then sort it by value.
The user interface is simple it shows what is the input the user want to sort and the other is the output that shows the sorted list bottom to top and the best horse

# Design

The program is simple, the user have three options for the input the user want to sort, it processes the value through bubble sort and display the sorted values of the horses bottom to top and it tells you which horse is the better one in the desired attribute.

The program follows this process:
1. Input: Horse data from Minecraft
2. Process: Sort horses using Bubble Sort
3. Output: Sorted list and best horse

# Algorithm Used

# Bubble Sort
Bubble Sort works by repeatedly comparing adjacent horses and swapping them if they are in the wrong order.

Steps:
1. Compare two horses
2. Swap if needed
3. Repeat until fully sorted

# Testing

The program was tested with:
- Multiple horses with different values
- Duplicate horses (to ensure they are ignored)
- Invalid entities (non-horses)
- Missing data cases

The results showed that:
- Horses are correctly collected
- Sorting works properly
- The best horse is correctly identified

# How to run
- Install dependencies:
  pip install keyboard pyperclip gradio
- Run the Horse Analyzer 3000.py
- Open minecraft:
   In minecraft
     - Go to a horse
     - Press "K" on your keyboard to collect the data
- Choose the desired attribute
- Click submit 
       
# Alternatively:
https://huggingface.co/spaces/GatoPretoo/CISC-121-FINAL-PROJECT

# Note

Due to platform limitations, the Hugging Face version cannot access the keyboard or clipboard.

Instead, users must manually paste the F3 + I data from Minecraft.

The local version supports automatic data collection using a keybind.
<img width="1895" height="872" alt="Screenshot 2026-04-06 181110" src="https://github.com/user-attachments/assets/59910ba7-c0b1-4148-96db-2265efe66aca" />
<img width="1887" height="839" alt="Screenshot 2026-04-06 181231" src="https://github.com/user-attachments/assets/f45651b8-5b74-4172-ac3d-21dc84e10a3f" />
<img width="1856" height="454" alt="Screenshot 2026-04-06 181244" src="https://github.com/user-attachments/assets/89cd17a9-4cea-4593-b5e1-e9e152827b9e" />
<img width="1918" height="459" alt="Screenshot 2026-04-06 181254" src="https://github.com/user-attachments/assets/c496c6b4-d98e-42b5-b8dc-204e8ca066eb" />
<img width="1904" height="852" alt="Screenshot 2026-04-06 180401" src="https://github.com/user-attachments/assets/79a640e3-6b7a-46f6-9187-98616e5b40ec" />
<img width="1823" height="484" alt="Screenshot 2026-04-06 181311" src="https://github.com/user-attachments/assets/0fb65e13-ec9a-4d66-9997-64ac2d94fff5" />

# Author

Lucca Meira Bassani (aka GatoPretoooo)

# Acknowledgement

- This program has two versions due to platform limitations. The local version supports automatic data collection, while the deployed version requires manual inputs
- The idea for this program was based on a earlier project that me and a friend developed two years ago.
- I would like to acknowledge the use of online resources and tools that helped me develop this project. 
- I used Python documentation and Gradio documentation to understand how to build the user interface.
- AI was used to help debug, improve code structure and understanding certain programming concepts 
