from django.core.management.base import BaseCommand
from job.models import Skill

class Command(BaseCommand):
    help = 'Add predefined skills to the database'

    def handle(self, *args, **kwargs):
        skills = [
            "Python Programming", "JavaScript Development", "Java Programming", 
            "Data Analysis", "Machine Learning", "Web Development", 
            "Mobile App Development", "UX/UI Design", "Cloud Computing", 
            "Cybersecurity", "Project Management", "Digital Marketing", 
            "SEO Optimization", "Graphic Design", "Software Testing", 
            "Database Management", "Agile Methodologies", "DevOps Practices", 
            "Blockchain Technology", "React Development", "Angular Development", 
            "C# Programming", "C++ Programming", "Ruby on Rails", 
            "RESTful API Development", "Data Visualization", "Business Analysis", 
            "Content Writing", "Social Media Management", "Public Speaking", 
            "Negotiation Skills", "Time Management", "Financial Analysis", 
            "E-commerce Management", "Technical Support", "Video Editing", 
            "Photography", "HTML/CSS Development", "SQL Programming", 
            "Data Science", "Networking Fundamentals", "Mobile UX Design", 
            "User Research", "Salesforce Administration", "ITIL Framework", 
            "Statistical Analysis", "Virtualization Technologies", "SAP ERP", 
            "TensorFlow", "Game Development"
        ]
        
        for skill_name in skills:
            Skill.objects.create(name=skill_name)
            
        self.stdout.write(self.style.SUCCESS('Successfully added 50 skills to the database.'))
