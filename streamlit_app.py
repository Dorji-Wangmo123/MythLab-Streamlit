import streamlit as st
from pathlib import Path
import html

st.set_page_config(page_title='MythLab | Project Showcase', page_icon='🐉', layout='wide', initial_sidebar_state='expanded')
ROOT = Path(__file__).resolve().parent
st.markdown('''<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Inter:wght@400;500;600;700&display=swap');
.stApp{background:linear-gradient(145deg,#061523,#0b2434);color:#eee7d6;font-family:Inter,sans-serif}
[data-testid="stSidebar"]{background:#04121e;border-right:1px solid #66512c}
[data-testid="stSidebar"] *{color:#eee7d6!important}
h1,h2,h3{color:#e4b65b!important;font-family:Cinzel,serif!important}
p,li{line-height:1.7}
[data-testid="stMetric"]{background:#102d3e;border:1px solid #80602c;border-radius:15px;padding:16px}
.stButton>button{background:#123246;color:#f6e6bf;border:1px solid #ad873f;border-radius:12px}
.stButton>button:hover{background:#d8a84f;color:#071523}
.hero{background:linear-gradient(110deg,#0e3042,#081824);border:1px solid #9e783b;border-radius:22px;padding:38px 35px;margin:12px 0 25px}
.kicker{color:#e3b85c;letter-spacing:2px;font-weight:700;font-size:12px}
.hero h1{font-size:3.5rem;margin:10px 0}
.panel{background:#102c3c;border:1px solid #5d4a2b;border-radius:16px;padding:22px;margin:9px 0 18px;min-height:145px}
.panel h3{font-size:1.18rem;margin-top:0}
.small{color:#bfcbd0;font-size:.95rem}
/* Readable dark tables for presentation */
.myth-table-wrap{overflow-x:auto;margin:18px 0 28px}
.myth-table{width:100%;border-collapse:separate;border-spacing:0;background:#102c3c;border:1px solid #8d713e;border-radius:14px;overflow:hidden;color:#f5ead0;font-size:1rem}
.myth-table th{background:#183b4e;color:#f3c66d;font-weight:700;text-align:left;padding:15px 17px;border-bottom:1px solid #8d713e}
.myth-table td{background:#102c3c;color:#f5ead0;padding:14px 17px;border-bottom:1px solid #385060;vertical-align:top;line-height:1.5}
.myth-table tr:nth-child(even) td{background:#153448}
.myth-table tr:last-child td{border-bottom:none}
.myth-table .pass{color:#80dfae;font-weight:700}
</style>''',unsafe_allow_html=True)

PAGES=['Home','Project Overview','Problem & Solution','Aim & Objectives','Main Features','System Design','Testing & Results','Challenges & Improvements','Team & GitHub','Conclusion & References']
with st.sidebar:
    st.markdown('## 🐉 MythLab')
    st.caption('Explore. Learn. Believe.')
    st.divider()
    page=st.radio('Explore the presentation',PAGES,label_visibility='collapsed')
    st.divider()
    st.caption('PRG304 GUI Programming · 2026')
    st.caption('Samtse College of Education')

def heading(kicker,title,description=''):
    st.markdown(f'<div class="kicker">{kicker.upper()}</div>',unsafe_allow_html=True)
    st.title(title)
    if description:st.write(description)

def presentation_table(headers, rows, status_column=None):
    """Show high-contrast tables that stay readable with our dark theme."""
    head = ''.join(f'<th>{html.escape(str(item))}</th>' for item in headers)
    body = ''
    for row in rows:
        cells = ''
        for index, value in enumerate(row):
            cls = ' class="pass"' if index == status_column else ''
            cells += f'<td{cls}>{html.escape(str(value))}</td>'
        body += f'<tr>{cells}</tr>'
    st.markdown(
        f'<div class="myth-table-wrap"><table class="myth-table">'
        f'<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>',
        unsafe_allow_html=True
    )

def panel(title,body):
    st.markdown(f'<div class="panel"><h3>{title}</h3><div class="small">{body}</div></div>',unsafe_allow_html=True)

if page=='Home':
    st.markdown('''<div class="hero"><div class="kicker">GROUP 1 · PRG304 GUI PROGRAMMING</div><h1>MythLab</h1><p>Exploring myths, legends and mythical creatures of Bhutan and beyond.</p><p style="color:#e3b85c">A digital mythology library built with Python, Tkinter and SQLite.</p></div>''',unsafe_allow_html=True)
    if (ROOT/'mythlab_preview.png').exists():
        st.image(str(ROOT/'mythlab_preview.png'),caption='MythLab visual from the project presentation',use_container_width=True)
    st.subheader('Explore our project')
    cols=st.columns(3)
    for col,(t,d) in zip(cols,[('📖 Myths & Legends','Explore cultural stories and detailed myth information.'),('🐉 Mythical Creatures','Discover creatures from Bhutan and other traditions.'),('🧩 Interactive Features','Quiz, favourites, regions and a personal task dashboard.')]):
        with col:panel(t,d)
    st.info('Use the left sidebar to move through the presentation during your group demonstration.')
elif page=='Project Overview':
    heading('Introduction','Project Overview','MythLab is a Python desktop application for exploring myths, legends and mythical creatures, with a focus on Bhutan and selected stories from other countries.')
    a,b,c=st.columns(3)
    with a:panel('📚 Myths and Legends','Browse traditional stories and read detailed information.')
    with b:panel('🐲 Mythical Creatures','Explore legendary beings and their cultural background.')
    with c:panel('🌏 Regions','Discover stories connected to different places.')
    st.subheader('Who is it for?')
    st.write('Students and teachers, people interested in Bhutanese culture, readers of myths and legends, and general users.')
    st.subheader('Project Scope')
    st.write('Browse myths and stories · Explore creatures · Discover regions · Take quizzes · Save favourites · Manage personal tasks')
elif page=='Problem & Solution':
    heading('Why we built it','Problem & Solution')
    a,b=st.columns(2)
    with a:
        st.subheader('The problem')
        for x in ['Mythological information is scattered across different sources.','Stories can be difficult to explore and organise.','Cultural stories may be overlooked.']:st.write('• '+x)
    with b:
        st.subheader('Our solution')
        for x in ['A user-friendly desktop application.','Organised myth, creature and region sections.','Search and filtering features.','SQLite database for structured storage.']:st.write('• '+x)
elif page=='Aim & Objectives':
    heading('Our direction','Aim & Objectives')
    panel('Project Aim','Develop an interactive desktop application that makes myths, legends and mythical creatures easier to explore and learn about.')
    for i,x in enumerate(['Design the interface using Tkinter.','Store and manage information using SQLite.','Organise myths, creatures and regions.','Provide search and filtering.','Include quizzes and additional user features.'],1):st.write(f'**{i}.** {x}')
elif page=='Main Features':
    heading('What users can do','Main Application Features')
    features=[('🏠 Home','Landing page and access to sections.'),('📖 Myths','Browse and read myth details.'),('🐉 Creatures','Explore mythical creatures and stories.'),('📍 Regions','Explore places and related information.'),('❓ Quiz','Test mythology knowledge.'),('♥ Favourites','Save items users like.'),('☑ My Tasks','Manage personal tasks.'),('ℹ About','Learn about the project.')]
    for start in range(0,len(features),4):
        cols=st.columns(4)
        for col,(t,d) in zip(cols,features[start:start+4]):
            with col:panel(t,d)
    st.subheader('Application preview')
    if (ROOT/'mythlab_preview.png').exists():st.image(str(ROOT/'mythlab_preview.png'),use_container_width=True)
elif page=='System Design':
    heading('Behind the interface','System Design & Technologies')
    st.table({'Technology':['Python','Tkinter','SQLite','Pillow','VS Code','GitHub'],'Purpose':['Programming language','Graphical interface','Database','Image display','Development','Version control']})
    st.subheader('How the system works')
    for i,x in enumerate(['User opens MythLab and enters through Welcome/Login.','User navigates using the sidebar.','Tkinter receives clicks and other actions.','Python processes actions and requests data.','SQLite stores or retrieves information.','The application displays the results.'],1):st.write(f'**Step {i}:** {x}')
    st.caption('Original project files include main.py, welcome.py, myths.py, myth_detail.py, creatures.py, regions.py, quiz.py, task.py, about.py, database.py and assets/.')
elif page=='Testing & Results':
    heading('Quality checks','Testing & Results')
    st.write('Our group tested the main application features during development to check that they worked as intended. The results are summarised below.')
    presentation_table(
        ['Area', 'What was checked', 'Result'],
        [
            ('Navigation', 'Pages open correctly', 'Pass'),
            ('Myths', 'Myth cards and details display', 'Pass'),
            ('Creatures', 'Creature information displays', 'Pass'),
            ('Regions', 'Region information displays', 'Pass'),
            ('Database', 'Information is retrieved from SQLite', 'Pass'),
            ('Quiz', 'Questions and answers function', 'Pass'),
            ('Tasks', 'Task actions update stored information', 'Pass'),
        ],
        status_column=2
    )
elif page=='Challenges & Improvements':
    heading('Learning through development','Challenges & Future Improvements')
    presentation_table(
        ['Challenge', 'How we addressed it'],
        [
            ('Connecting different page modules', 'Used separate Python modules'),
            ('Managing image paths', 'Organised images in the assets folder'),
            ('Connecting Tkinter and SQLite', 'Used database helper functions'),
            ('Debugging errors', 'Tested features and corrected errors'),
            ('Coordinating group development', 'Collaborated through GitHub'),
        ]
    )
    a,b=st.columns(2)
    with a:
        st.subheader('Current limitations')
        st.write('Desktop-based application; content can be expanded; further testing and refinement; security and backup improvements.')
    with b:
        st.subheader('Future improvements')
        st.write('More stories and regions; improved quizzes; stronger account security and backups; more interactive learning features.')
elif page=='Team & GitHub':
    heading('Working together','Team & GitHub')
    st.write('**Group 1:** Tshering Deki, Dorji Wangmo, Cheki Uden, Sonam Wangchuk, Younten Zangmo and Kalpana Mongar.')
    panel('Collaboration','Responsibilities were shared among six group members. The application was developed in separate modules, integrated, tested and improved together.')
    st.link_button('Open MythLab GitHub Repository','https://github.com/Dorji-Wangmo123/MythLab')
    st.write('GitHub was used to track changes, collaborate and share source code.')
    st.caption('Tutor: Anup Gurung · Academic year: 2026')
elif page=='Conclusion & References':
    heading('Final thoughts','Conclusion')
    panel('What we achieved','MythLab provides a digital way to explore myths, legends and creatures. Tkinter provides the graphical interface, SQLite manages stored information, and separate modules help organise the application.')
    st.write('The project helped the group practise Python programming, GUI development, database integration and teamwork.')
    st.subheader('Documentation & References')
    for name,url in [('Python documentation','https://docs.python.org/3/'),('Tkinter documentation','https://docs.python.org/3/library/tkinter.html'),('SQLite documentation','https://www.sqlite.org/docs.html'),('Pillow documentation','https://pillow.readthedocs.io/'),('GitHub documentation','https://docs.github.com/')]:st.markdown(f'- [{name}]({url})')
    st.success('Thank you! Questions and discussion.')
