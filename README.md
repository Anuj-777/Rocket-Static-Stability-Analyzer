\# 🚀 Rocket Static Stability Analyzer



!\[Rocket Visualization](screenshots/rocket\_visualization.png)



A Python-based engineering application that calculates the \*\*static stability margin\*\* of a rocket and provides a graphical visualization of the rocket, including the \*\*Center of Gravity (CG)\*\* and \*\*Center of Pressure (CP)\*\*.



The project combines aerospace engineering principles with Python programming to help visualize rocket stability in an intuitive way.



\---



\## 📖 Overview



Static stability is one of the most important parameters in rocket design. This application allows users to:



\- Enter rocket dimensions and aerodynamic parameters.

\- Calculate the static margin in calibers.

\- Determine whether the rocket is stable.

\- Generate a graphical representation of the rocket showing:

&#x20; - Rocket body

&#x20; - Nose

&#x20; - Tail fins

&#x20; - Center of Gravity (CG)

&#x20; - Center of Pressure (CP)

&#x20; - Stability status



\---



\## ✨ Features



\- 🚀 Rocket stability analysis

\- 📏 Static Margin calculation

\- 📍 Center of Gravity (CG) visualization

\- 📍 Center of Pressure (CP) visualization

\- 📊 Automatic stability assessment

\- 🎨 Graphical rocket visualization using Matplotlib

\- 💾 Automatic export of the generated figure



\---



\## 📐 Static Margin Formula



The static margin is calculated using:



\\\[

\\text{Static Margin} = \\frac{CP - CG}{Diameter}

\\]



Where:



\- \*\*CG\*\* = Center of Gravity

\- \*\*CP\*\* = Center of Pressure

\- \*\*Diameter\*\* = Rocket diameter



The result is expressed in \*\*calibers\*\*, a standard metric used in rocket stability analysis.



\---



\## 🖥️ Example Input



```text

Rocket Length (m):          2.0

Center of Gravity (m):      0.8

Center of Pressure (m):     1.2

Rocket Diameter (m):        0.075

```



\---



\## 📈 Example Output



```text

\----- RESULTS -----



Static Margin = 5.33 calibers

Status        = STABLE

```



\---



\## 📷 Sample Visualization



The application automatically generates and saves the following visualization:



!\[Rocket Visualization](screenshots/rocket\_visualization.png)



\---



\## 📁 Project Structure



```text

Rocket-Static-Stability-Analyzer/

│

├── main.py

├── calculations.py

├── visualization.py

├── screenshots/

│   └── rocket\_visualization.png

├── README.md

├── requirements.txt

├── LICENSE

└── .gitignore

```



\---



\## ⚙️ Installation



Clone the repository



```bash

git clone https://github.com/Anuj-777/Rocket-Stability-Calculator.git

```



Navigate into the project directory



```bash

cd Rocket-Stability-Calculator

```



Install the required packages



```bash

pip install -r requirements.txt

```



Run the application



```bash

python main.py

```



\---



\## 🛠 Technologies Used



\- Python 3

\- Matplotlib



\---



\## 🎯 Future Improvements



\- Graphical User Interface (GUI)

\- Interactive parameter editing

\- Unit conversion support

\- CSV input/output

\- Multiple rocket configurations

\- 3D rocket visualization

\- Aerodynamic coefficient estimation

\- Stability optimization tools



\---



\## 📚 Engineering Concepts Used



\- Static Stability

\- Center of Gravity (CG)

\- Center of Pressure (CP)

\- Static Margin

\- Data Visualization

\- Modular Programming



\---



\## 👨‍💻 Author



\*\*Anuj Mangaj\*\*



Aerospace Engineering Student



Interested in:

\- Rocket Dynamics

\- Flight Simulation

\- MATLAB

\- Python

\- Engineering Software Development



\---



\## 📄 License



This project is licensed under the MIT License.



\---



\### ⭐ If you found this project interesting, consider giving it a star!

