from pathlib import Path
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='DembarembaFarmPage', page_icon=':palm_tree:', layout='wide')


img_wheat_form=Image.open('assets/wheatfeild.jpeg')
img_maize_form=Image.open('assets/maize.jpg')
img_garlic_form=Image.open('assets/garlic.jpg')
img_sugarcane_form=Image.open('assets/Sugarcane.jpg')
img_cattle_form=Image.open('assets/cattle.jpg')
img_goats_form=Image.open('assets/goats.jpg')
img_hens_form=Image.open('assets/hens.jpg')
img_ploughing_form=Image.open('assets/ploughing.jpeg')


selected = option_menu(
    menu_title=None,
    options=['Home', 'Support Us', 'About'],
    icons=['house-fill', 'bag-plus-fill', 'file-person-fill'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal',

)

if selected == 'Home':
    with st.container():
        st.subheader('Hi:wave:, Welcome to Dembaremba Farm Page where good things grow')
        st.write('Glad to have you back my farmer , my buyer , my information seeker !!!!')
        st.header(
            'Agriculture is our wisest persuit. The most healthful, most useful and most noble employment of man.')

        st.write(
            '''
            Over the last decades, Our farming has been driven by the objective to increase food production. The
            global market, in particular the availability of cheap inputs (mineral fertilisers, animal feed), has introduced
            the logic of economies of scale. The intensification of farming systems was associated with specialisation of 
            farms and regions, leading to a separation of livestock and cash crop production. This had drastic 
            environmental consequences: water pollution due to an excess of manure and slurries, soil degradation, 
            depletion of natural resources, loss of biodiversity and lower resilience to climate change. But us as region 1,
            we are endowered with blessings as we do mixed farming on the same piece of land than any other regions, looking at
            our sustainable climatic conditions. 
            '''
        )
        st.write('No farm too far!')
        st.write("[Our location 🚩](https://goo.gl/maps/GPW2rJLVC2KNjxjL6)")

        with st.container():
            st.write('---')
            left_column, right_column = st.columns(2)
        with left_column:
            st.header('Learn Zim Farming With Us')

# ----PATH SETTINGS----
        current_dir = Path(__file__).parent if __file__ in locals() else Path.cwd()
        css_file = current_dir / 'style' / 'style.css'
        pdf1_file = current_dir / 'assets' / 'Agritex_Pfumbvuza_Broucher.pdf'
        pdf2_file = current_dir / 'assets' / 'Conservation Farming and the Food Security-Insecurity.pdf'
        pdf3_file = current_dir / 'assets' / 'Policy Brief_38_Working towards climate-resilient agricultural systems in Zimbabwe .pdf'

        # ----LOAD CSS,PDF----
        with open(css_file) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        with open(pdf1_file, 'rb') as pdf_file:
            PDFbyte = pdf_file.read()

        with open(css_file) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        with open(pdf2_file, 'rb') as pdf_file:
            PDFbyte = pdf_file.read()

        with open(css_file) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        with open(pdf3_file, 'rb') as pdf_file:
            PDFbyte = pdf_file.read()

        with st.container():
            left_column, right_column = st.columns(2)

            with left_column:
                st.download_button(
                    label='Download Pdf (1)',
                    data=PDFbyte,
                    file_name=pdf1_file.name,
                    mime='application/octet-stream',

                )
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.download_button(
                    label='Download Pdf (2)',
                    data=PDFbyte,
                    file_name=pdf1_file.name,
                    mime='application/octet-stream',

                )
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.download_button(
                    label='Download Pdf (3)',
                    data=PDFbyte,
                    file_name=pdf1_file.name,
                    mime='application/octet-stream',

                )


        with st.container():
            st.write('#')
            st.write('Social Media Platforms')
            SOCIAL_MEDIA= {
                    'Youtube':'https://www.bing.com/ck/a?!&&p=4a6df0d6da6d607bJmltdHM9MTY4Njg3MzYwMCZpZ3VpZD0zMjJhZDhkOS00NTZhLTY0ZTMtMTk0ZC1jYTg3NDQ4ZDY1MGQmaW5zaWQ9NTEzNQ&ptn=3&hsh=3&fclid=322ad8d9-456a-64e3-194d-ca87448d650d&u=a1L3ZpZGVvcy9zZWFyY2g_cT15b3V0dWJlK3ppbWJhYndlK2xpbmsrYWJvdXQrdGFsa2luZytmYXJtaW5nJnFwdnQ9eW91dHViZSt6aW1iYWJ3ZStsaW5rK2Fib3V0K3RhbGtpbmcrZmFybWluZyZGT1JNPVZEUkU&ntb=1',
                    'Twitter':'https://www.bing.com/ck/a?!&&p=92835c73ef35e6cbJmltdHM9MTY4Njg3MzYwMCZpZ3VpZD0zMjJhZDhkOS00NTZhLTY0ZTMtMTk0ZC1jYTg3NDQ4ZDY1MGQmaW5zaWQ9NTE4Nw&ptn=3&hsh=3&fclid=322ad8d9-456a-64e3-194d-ca87448d650d&psq=twitter+link+about+zimbabwe+farming&u=a1aHR0cHM6Ly90d2l0dGVyLmNvbS9ad0FncmljdWx0dXJl&ntb=1',
                    'Facebook': 'https://www.bing.com/ck/a?!&&p=4a744da93c4f4178JmltdHM9MTY4Njg3MzYwMCZpZ3VpZD0zMjJhZDhkOS00NTZhLTY0ZTMtMTk0ZC1jYTg3NDQ4ZDY1MGQmaW5zaWQ9NTE3Mg&ptn=3&hsh=3&fclid=322ad8d9-456a-64e3-194d-ca87448d650d&psq=facebook+link+about+zimbabwe+farming&u=a1aHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2dyb3Vwcy8xMzk1NTE4NDY1ODgwMDUv&ntb=1',
                    'ZBC':'https://www.bing.com/ck/a?!&&p=8937eac2d1b13dd8JmltdHM9MTY4Njg3MzYwMCZpZ3VpZD0zMjJhZDhkOS00NTZhLTY0ZTMtMTk0ZC1jYTg3NDQ4ZDY1MGQmaW5zaWQ9NTE5MA&ptn=3&hsh=3&fclid=322ad8d9-456a-64e3-194d-ca87448d650d&psq=zbc+zimbabwe+link+about+talking+farming&u=a1aHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL1pCQ1RWVGFsa2luZ2Zhcm1pbmcv&ntb=1',
        }

            cols=st.columns(len(SOCIAL_MEDIA))
        for index,(platform,link)in enumerate(SOCIAL_MEDIA.items()):
            cols[index].write(f'[{platform}]({link})')






#----ACCOPLISHMENTS----
        with st.container():
            st.write('---')
            left_column, right_column = st.columns(2)
            with left_column:
                st.header('Our Accomplishments')
                st.write('##')
                st.write(
                    '''
                    IN OUR COMMUNITY WE HAVE :
                    - 🏆Taught new farmers agricultural skills
                    - 🏆Increased employment.
                    - 🏆Constructed village roads.
                    - 🏆Electrified our home.
                    - 🏆Prevailed agricultural shows.
                    - 🏆Donated to funerals.
                    '''
                )

#----OUR PRODUCTS----
        with st.container():
            st.write('----')
            st.header('Available Products (Farm fresh, Home Grown Quality Since 2003)')
            st.write('##')
            st.write('Let us look at our crops')
            image_column,text_column=st.columns((1,2))
            with image_column:
                st.image(img_wheat_form)
            with text_column:
                st.subheader('Winter Wheat')
                st.write(
                    '''
                    Save and earn more!
                    Wheat is the second most important cereal after maize in the food security basket
                    of Zimbabwe. The production of most products such as bread, buns and cookies has made 
                    the crop popular with the general population.Each year we sow wheat for the better of the nation 
                    harvesting more than 5 tonnes,saving for stock feed but sales are widely supplied in the month of 
                    November without any doubt.The nation recommends these crop giving hand with the supply of presidential
                    inputs considering your hectares which keeps us as farmers to put more efforts. Our main target is
                    to avoid unnecessary imports whilst we have fertile lands.
                    '''
                )


        with st.container():
            image_column,text_column=st.columns((1,2))
            with image_column:
                st.image(img_maize_form)
            with text_column:
                st.subheader('Maize greens/grains')
                st.write(
                    '''
                    Farm fresh makes our way of living!
                    We are predominated to a high rainfall area,
                    we then take maize production from October to December depending on 
                    the time of maturity.Each year we produce 5-10 tones of dried maize,marketing
                    to the Grain Marketing Board , local sales as well. Maize has been giving us a way of life
                    since the 80s, Nationally Zimbabwean stapple crop is maize , where citizens do variety of dishes.
                    We are sure that citizens may be doing western dishes but they will never quit maize as it falls
                    under the most recommended energy giving nutrient. by Takudzwa Dembaremba : "A day in the December holidays
                    I have been laughing at my diaspora brother being convinced to carry at a 10kg mealie meal
                    sack back home so he can do bota, a breakfast dish like Cerevita for his children."
                    '''
                )

        with st.container():
            image_column,text_column=st.columns((1,2))
            with image_column:
                st.image(img_garlic_form)
            with text_column:
                st.subheader('Garlic strongest herb')
                st.write(
                    '''
                    Bringing the farm to your healthy!
                    Garlic lowers blood pressure, avoids winter cold, prevents all cancer types, balances
                    blood sugar and weight loss herb, that is why we never get tired producing each and every year
                    because the demand is higher than the production. Looking in Zimbabwe garlic production has increased by
                    more than 600 percent. Most farmers produce during the late summer between February and May, at this time of year
                    temperatures are not excessively high and good soil moisture, fairly spacing between rows will depend on the 
                    method of planting and available equipment for cultivation. Our piece of land usually produce 500kgs +
                    each season.
                    '''
                )



        with st.container():
            image_column,text_column=st.columns((1,2))
            with image_column:
                st.image(img_sugarcane_form)
            with text_column:
                st.subheader('Sweet Sugarcane')
                st.write(
                    '''
                    Healthy from the heartland!
                    Sugarcane is grown under the canal irrigation in the low veld
                    areas, varieties include NCo376 and N14 are the mostly available,
                    non-organic fertilisation it is natural sweet sap. Sugarcane can be used as a
                    wind break to avoid crop damage, somtimes planting sugarcane in feild banks is really advised
                    as it saves weak stem crops from breaking during wind sessions. Zimbabwe is also majored as
                    one of the best refining company, so it saves a lot from nations with it's exports even local
                    residents can afford prices from supermarkets after beneficiary of products. 
                    '''
                )


        st.write('##')
        st.write('Let us see Animal Husbandry')

        with st.container():
            image_column,text_column=st.columns((1,2))
            with image_column:
                st.image(img_cattle_form)
            with text_column:
                st.subheader('Cattle')
                st.write(
                    '''
                    Our farms, your table!
                    Cattle is now new currency amid crippling inflation. Zimabweans are 
                    scrambling to buy cattle to store the value of their wealth amid
                    a collapsing currency fanned by the galloping inflation. Cattle have contributing to the survival
                    of humans for thousands of years, critically a daily source of food and nutrition, of much
                    needed income, and of nitrogen-rich manure for replenishing soils and other uses.
                    They also full fill a wide variety of socio-cultural roles. In conclusion we can say cattle 
                    are a source of economy stability if monitored very well from diseases and other hazards 
                    '''
                )

        with st.container():
            image_column,text_column=st.columns((1,2))
            with image_column:
                st.image(img_goats_form)
            with text_column:
                st.subheader('Goats')
                st.write(
                    '''
                    The best farms are friendship!
                    In the recent years from 2018 in the economy hardships, to farmers wealthy and assets
                    have been backing their financial accounts. Parents with children in schools have been 
                    covering school fees, student expense and home expenses as well, with livestock. Those 
                    expenses were covered with goat selling live or slaughtered. Butcheries,hotels and restaurants
                    have been earning till now there are earning more. Goats are important animals that require less 
                    expenses to keep at the same time each year they can bread up to 4 kids. Goats are important. 
                    '''
                )

        with st.container():
            image_column,text_column=st.columns((1,2))
            with image_column:
                st.image(img_hens_form)
            with text_column:
                st.subheader('Poultry')
                st.write(
                    '''
                    What grows together goes better!
                    In the long time, road runner farming on a big scale will be more profitable and generate
                    more money than broiler farming since the birds may be sold as meat after producing eggs,
                    albeit at a lower price than broilers. The road runner chain is one of the fastest growing 
                    sectors in Zimbabwe during the last decades, with an estimated growth rate of 26% in three years.
                    Road runners are safe in a way that there do not need a lot chemicals for their healthy even
                    feeding they grow naturally in any conditions, looking at food saving they can only be fed once a day or 
                    more and the rest they cover for themselves.
                    '''
                )


#----CONTACT FORM----
        st.write('---')
        st.write('##')
        st.header('Get In Touch With Us📬')
        contact_form = '''
            <form action='https://formsubmit.co/takudzwadembaremba8@gmail.com' method ='POST'>
                <input type='hidden' name ='_captcha' value='false'>
                <input type ='text' name='name' placeholder='Your Name' required>
                <input type ='email' name='email' placeholder='Your email' required>
                <textarea name='message' placeholder='Your message here' requires></textarea>
                <button type ='submit'>Send</button>
            </form>
            '''
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
        st.write('----')

#----SUPPORT US FORM----
if selected == 'Support Us':

    with st.container():
        st.header('TO GIVE YOUR BEST IS TO RECEIVE THE BEST🎁🎁🎁🎁🎁🎁')
        st.write('##')
        with st.container():
            left_column, right_column = st.columns((1, 2))
        with left_column:
            st.subheader(
                '''
                A lot of farmers are struggling with shortages of farming equipment such as tractors , planters and irrigating tools. 
                Over the past years products have been very low due to late planting , 
                slow cultivation which was bringing pest and diseases to our crops at an early stage. Our main goals 
                include increasing food production to reduce imports but have a lot of exports. Another goal , as 
                Zimbabweans are fighting substance abuse to young boys and girls, Us as farmers we think employment creation will
                give an opportunity to an end of substance abuse, the more farms get resources the more employment is created.
                '''
            )
            st.write('---')
            st.write('🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾🧑🏻‍🌾')

        with right_column:
            st.image(img_ploughing_form)

        st.write('##')
        st.write('----')
        st.subheader('Would it be Ok for you to give a hand , if yes we are glad to receive your donation.')
        st.write('Contact : call📞+263 712 758 048')
        st.write('Whatsapp : text💬+263 784 244 239')
        st.write("[Our location 🚩](https://goo.gl/maps/GPW2rJLVC2KNjxjL6)")
        st.write('----')

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


    local_css('style/style.css')

#----ABOUT FORM---
if selected == 'About':
    current_dir = Path(__file__).parent if __file__ in locals() else Path.cwd()
    css_file = current_dir / 'style' / 'style.css'
    profile_pic = current_dir / 'assets' / 'profile.png'

    with st.container():
        with open(css_file)as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
            profile_pic =Image.open(profile_pic)
        st.write('#')
        st.write('----')
        image_column,text_column=st.columns((1,2))
        with image_column:
            st.image(profile_pic,width=230)

        with text_column:
            st.write('👉Developer : Takudzwa Dembaremba')
            st.write('👉Experience : High school graduate,currently a self taught Python programmer......(doing creations in my room)')
            st.write('👉Contact : +263 780 499 605📞💬')
            st.write('Important notice!!')
            st.write(
                '''
                By using this web you indicate your agreement to our End User Licence Agreement
                and give your consent to the use of your data to deliver more relevant advertising.
                 For more information on how we use your data , please contact +263 780 499 605.
                '''
            )
            st.write('Recommended to watch video ▶')
            st.write("[my vlog 📺](http://www.youtube.com/@TakudzwaDembaremba)")
        st.write('---')
        st.write('Dedication to Jennifa Jaricha Dembaremba 1966-2014')
