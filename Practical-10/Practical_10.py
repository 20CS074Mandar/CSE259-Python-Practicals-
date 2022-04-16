from PIL import  Image
result_image=Image.open(r'C:\Users\manda\PycharmProjects\CSE259-Python-Practicals-\Practical-10\Capture.PNG')
final_result=result_image.convert('RGB')
final_result.save(r'C:\Users\manda\PycharmProjects\CSE259-Python-Practicals-\Practical-10\Capture.PDF',save_all=True)
print("PDF HAS BEEN CREATED!")