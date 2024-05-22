from bs4 import BeautifulSoup

html = """
<h2><span class="mw-headline" id="Births">Births</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=April_23&amp;action=edit&amp;section=5" title="Edit section: Births"><span>edit</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<ul><li><a href="/wiki/1141" title="1141">1141</a> (probable)<sup id="cite_ref-17" class="reference"><a href="#cite_note-17">[17]</a></sup> – <a href="/wiki/Malcolm_IV_of_Scotland" title="Malcolm IV of Scotland">Malcolm IV of Scotland</a> (d. 1165)</li>
<li><a href="/wiki/1185" title="1185">1185</a> – <a href="/wiki/Afonso_II_of_Portugal" title="Afonso II of Portugal">Afonso II of Portugal</a> (d. 1223)<sup id="cite_ref-18" class="reference"><a href="#cite_note-18">[18]</a></sup></li>
<li><a href="/wiki/1408" title="1408">1408</a> – <a href="/wiki/John_de_Vere,_12th_Earl_of_Oxford" title="John de Vere, 12th Earl of Oxford">John de Vere, 12th Earl of Oxford</a> (d. 1462)<sup id="cite_ref-19" class="reference"><a href="#cite_note-19">[19]</a></sup></li>
<li><a href="/wiki/1420" title="1420">1420</a> – <a href="/wiki/George_of_Pod%C4%9Bbrady" title="George of Poděbrady">George of Poděbrady</a>, King of Bohemia (d. 1471)</li>
<li><a href="/wiki/1464" title="1464">1464</a> – <a href="/wiki/Joan_of_France,_Duchess_of_Berry" title="Joan of France, Duchess of Berry">Joan of France, Duchess of Berry</a> (d. 1505)</li>
<li>1464   – <a href="/wiki/Robert_Fayrfax" title="Robert Fayrfax">Robert Fayrfax</a>, English Renaissance composer (d. 1521)</li>
<li><a href="/wiki/1484" title="1484">1484</a> – <a href="/wiki/Julius_Caesar_Scaliger" title="Julius Caesar Scaliger">Julius Caesar Scaliger</a>, Italian physician and scholar (d. 1558)</li>
<li><a href="/wiki/1500" title="1500">1500</a> – <a href="/wiki/Alexander_Ales" title="Alexander Ales">Alexander Ales</a>, Scottish theologian and academic (d. 1565)</li>
<li>1500   – <a href="/wiki/Johann_Stumpf_(writer)" title="Johann Stumpf (writer)">Johann Stumpf</a>, Swiss writer (d. 1576)</li>
<li><a href="/wiki/1512" title="1512">1512</a> – <a href="/wiki/Henry_FitzAlan,_19th_Earl_of_Arundel" class="mw-redirect" title="Henry FitzAlan, 19th Earl of Arundel">Henry FitzAlan, 19th Earl of Arundel</a>, Chancellor of the University of Oxford (d. 1580)</li>
<h2><span class="mw-headline" id="Deaths">Deaths</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=April_23&amp;action=edit&amp;section=6" title="Edit section: Deaths"><span>edit</span></a><span class="mw-editsection-bracket">]</span></span></h2>
<li><a href="/wiki/1516" title="1516">1516</a> – <a href="/wiki/Georg_Fabricius" title="Georg Fabricius">Georg Fabricius</a>, German poet, historian, and archaeologist (d. 1571)</li>
<li><a href="/wiki/1564" title="1564">1564</a> – <a href="/wiki/William_Shakespeare" title="William Shakespeare">William Shakespeare</a>, English playwright and poet (d. 1616)<sup id="cite_ref-20" class="reference"><a href="#cite_note-20">[20]</a></sup></li>
<li><a href="/wiki/1598" title="1598">1598</a> – <a href="/wiki/Maarten_Tromp" title="Maarten Tromp">Maarten Tromp</a>, Dutch admiral (d. 1653)</li></ul>

"""

soup = BeautifulSoup(html, 'html.parser')

births_span = soup.find('span', {'id': 'Births'})
deaths_span = soup.find('span', {'id': 'Deaths'})

if births_span and deaths_span:
    births_ul = births_span.find_next('ul')
    deaths_ul = deaths_span.find_next('ul')
    
    births_list_items = births_ul.find_all('li')
    
    formatted_births = []
    
    for item in births_list_items:
        formatted_births.append(item.get_text(strip=True))
    
    formatted_births_str = '\n'.join(formatted_births)
    print(formatted_births_str)
else:
    print("Births or Deaths span not found.")
