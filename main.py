import requests
import json
url = "http://localhost:3000/select?titleSlug="

def read_file(file):
    with open(file, 'r') as file:
        content = file.read()
        return content.split("\n")

def read_prob(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data))
        # print(data.get("question"))
        print("___")
        # print(data.get("exampleTestcases"))
    else:
        print(f"Failed to fetch data: {response.status_code}")

def create_file(filename:str):
    filename = filename.replace("-","_")+".py"
    with open("problems/"+filename, 'w') as f:
        f.write(
        """
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass

tests=[
    (
        (,),
        1
    ),(
        (,),
        1
    )
]
        
        """)


probs = read_file("probs")
for prob in probs:
    prob_url = url+prob
    # read_prob(prob_url)
    create_file(prob)