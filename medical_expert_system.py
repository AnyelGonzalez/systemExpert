from experta import *

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("diseases.txt")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		disease_s_file = open("Disease/" + disease + ".txt")
		disease_s_data = disease_s_file.read()
		s_list = disease_s_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		disease_s_file.close()
		# disease_s_file = open("Disease descriptions/" + disease + ".txt")
		# disease_s_data = disease_s_file.read()
		# d_desc_map[disease] = disease_s_data
		# disease_s_file.close()
		# disease_s_file = open("Disease treatments/" + disease + ".txt")
		# disease_s_data = disease_s_file.read()
		# d_treatment_map[disease] = disease_s_data
		# disease_s_file.close()
	

def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("The most probable disease that you have is %s\n" %(id_disease))
		print("A short description of the disease is given below :\n")
		print(disease_details+"\n")
		print("The common medications and procedures suggested by other real doctors are: \n")
		print(treatments+"\n")

# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#def identify_disease(headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever,sunken_eyes):
class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("¡Hola! Por medio de las siguentes preguntas vamos a determinar que tipo de 'Gripa' tiene el paciente")
		print("¿Siente alguno de los siguientes síntomas?")
		print("")
		yield Fact(action="find_disease")


	@Rule(Fact(action='find_disease'), NOT(Fact(fever=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(fever=input("Fiebre (si/no): ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(body_temperature=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(body_temperature=input("Temperatura corporal (es mayor 38.5) (si/no): ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(cough=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(cough=input("Tos (si/no): ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(type_cough=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(type_cough=input("Tipo Tos(conFlema/seca): ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(bugger=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(bugger=input("Moco (si/no): ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(nasal_congestion=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(nasal_congestion=input("Congestión nasal (si/no): ")))
	 
	@Rule(Fact(action='find_disease'), NOT(Fact(sneezing=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(sneezing=input("Estornudos (si/no): ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(throat_pain=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(throat_pain=input("Dolor de garganta (si/no): ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(discomfort_in_the_throat=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(discomfort_in_the_throat=input("Malestar en la garganta (si/no): ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(difficulty_breathing=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(difficulty_breathing=input("Dificultad para respirar (si/no): ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(phlegm=W())),salience = 1)
	def symptom_10(self):self.declare(Fact(phlegm=input("Flema (si/no): ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(threw_up=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(threw_up=input("Vómito (si/no): ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(diarrhea=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(diarrhea=input("Diarrea (si/no): ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(weakness_tiredness=W())),salience = 1)
	def symptom_13(self):
		self.declare(Fact(weakness_tiredness=input("Debilidad/Cansancio (si/no): ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(bone_pain=W())),salience = 1)
	def symptom_14(self):
		self.declare(Fact(bone_pain=input("Dolor en los huesos (si/no): ")))
	@Rule(Fact(action='find_disease'), NOT(Fact(lung_x_ray_with_spot=W())),salience = 1)
	def symptom_15(self):
		self.declare(Fact(lung_x_ray_with_spot=input("Rx del pulmón con mancha (si/no): ")))

		

	@Rule(Fact(action='find_disease'),Fact(fever="si"),Fact(body_temperature="si"),Fact(cough="si"),Fact(type_cough="seca"),Fact(bugger="no"),Fact(nasal_congestion="no"),Fact(sneezing="no"),Fact(throat_pain="si"),Fact(discomfort_in_the_throat="si"),Fact(difficulty_breathing="si"),Fact(phlegm="si"),Fact(threw_up="si"),Fact(diarrhea="si"),Fact(weakness_tiredness="si"),Fact(bone_pain="no"),Fact(lung_x_ray_with_spot="si"))
	def disease_0(self):
		self.declare(Fact(disease="Covid-19"))

	@Rule(Fact(action='find_disease'),Fact(fever="si"),Fact(body_temperature="no"),Fact(cough="si"),Fact(type_cough="conFlema"),Fact(bugger="si"),Fact(nasal_congestion="no"),Fact(sneezing="si"),Fact(throat_pain="no"),Fact(discomfort_in_the_throat="no"),Fact(difficulty_breathing="no"),Fact(phlegm="si"),Fact(threw_up="si"),Fact(diarrhea="si"),Fact(weakness_tiredness="no"),Fact(bone_pain="si"),Fact(lung_x_ray_with_spot="no"))
	def disease_1(self):
		self.declare(Fact(disease="Gripe"))

	@Rule(Fact(action='find_disease'),Fact(fever="no"),Fact(body_temperature="no"),Fact(cough="si"),Fact(type_cough="conFlema"),Fact(bugger="no"),Fact(nasal_congestion="si"),Fact(sneezing="si"),Fact(throat_pain="si"),Fact(discomfort_in_the_throat="si"),Fact(difficulty_breathing="no"),Fact(phlegm="no"),Fact(threw_up="no"),Fact(diarrhea="no"),Fact(weakness_tiredness="no"),Fact(bone_pain="no"),Fact(lung_x_ray_with_spot="no"))
	def disease_2(self):
		self.declare(Fact(disease="Resfrio"))

	# @Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	# def disease_3(self):
	# 	self.declare(Fact(disease="Tuberculosis"))

	# @Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	# def disease_4(self):
	# 	self.declare(Fact(disease="Asthma"))

	# @Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	# def disease_5(self):
	# 	self.declare(Fact(disease="Sinusitis"))

	# @Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	# def disease_6(self):
	# 	self.declare(Fact(disease="Epilepsy"))

	# @Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	# def disease_7(self):
	# 	self.declare(Fact(disease="Heart Disease"))

	# @Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	# def disease_8(self):
	# 	self.declare(Fact(disease="Diabetes"))

	# @Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	# def disease_9(self):
	# 	self.declare(Fact(disease="Glaucoma"))

	# @Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	# def disease_10(self):
	# 	self.declare(Fact(disease="Hyperthyroidism"))

	# @Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	# def disease_11(self):
	# 	self.declare(Fact(disease="Heat Stroke"))

	# @Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	# def disease_12(self):
	# 	self.declare(Fact(disease="Hypothermia"))

	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		print("")
		id_disease = disease
		# disease_details = get_details(id_disease)
		# treatments = get_treatments(id_disease)
		print("")
		print("La enfermedad más probable que tienes es %s\n" %(id_disease))
		# print("A short description of the disease is given below :\n")
		# print(disease_details+"\n")
		# print("The common medications and procedures suggested by other real doctors are: \n")
		# print(treatments+"\n")

	@Rule(Fact(action='find_disease'),
			Fact(fever=MATCH.fever),
			Fact(body_temperature=MATCH.body_temperature),
			Fact(cough=MATCH.cough),
			Fact(type_cough=MATCH.type_cough),
			Fact(bugger=MATCH.bugger),
			Fact(nasal_congestion=MATCH.nasal_congestion),
			Fact(sneezing=MATCH.sneezing),
			Fact(throat_pain=MATCH.throat_pain),
			Fact(discomfort_in_the_throat=MATCH.discomfort_in_the_throat),
			Fact(difficulty_breathing=MATCH.difficulty_breathing),
			Fact(phlegm=MATCH.phlegm),
			Fact(threw_up=MATCH.threw_up),
			Fact(diarrhea=MATCH.diarrhea),
			Fact(weakness_tiredness=MATCH.weakness_tiredness),
			Fact(bone_pain=MATCH.bone_pain),
			Fact(lung_x_ray_with_spot=MATCH.lung_x_ray_with_spot),NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,fever, body_temperature, cough, type_cough, bugger, nasal_congestion, sneezing, throat_pain, discomfort_in_the_throat, difficulty_breathing, phlegm, threw_up, diarrhea, weakness_tiredness, bone_pain, lung_x_ray_with_spot ):
		print("\nDid not find any disease that matches your exact symptoms")
		lis = [fever, body_temperature, cough, type_cough, bugger, nasal_congestion, sneezing, throat_pain, discomfort_in_the_throat, difficulty_breathing, phlegm, threw_up, diarrhea, weakness_tiredness, bone_pain, lung_x_ray_with_spot ]
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if_not_matched(max_disease)


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("¿Le gustaría diagnosticar algunos otros síntomas?")
		if input() == "no":
			exit()
		#print(engine.facts)