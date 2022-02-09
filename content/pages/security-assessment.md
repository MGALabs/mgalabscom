title: Security Assessment
date: 2022-01-31 10:22
save_as: security-assessment.html
menu_order: 0
hide_menu: True

{% from 'row.html' import row %}
{% from 'row.html' import hero %}

<!-- hero(
    Hero Title,
    Hero Content (accepts html),
    Hero Image
    Hero Image alt Text
-->

{{ hero("Security Assessment",
    "MGALabs offre servizi professionali destinati ad accompagnare nel proprio percorso tecnologico qualsiasi azienda già avviata o soluzioni mirate a sviluppare in termini di progettazione ed implementazione di infrastrutture IT qualsiasi attività di business nascente.",
    "{static}/images/security-assessment.png",
    "Security Assessment") }}

<!-- row(
    Row Title - can be empty (""),
    Row Content (accepts html),
    Row Image - leave empty ("") to render full-width text
    Row Image alt Text
-->

{{ row("Row Title",
    "
    <p>La metodologia per il Vulnerability Assessment infrastrutturale permette di individuare tutte le vulnerabilità, potenziali o presenti, all'interno dei sistemi della rete aziendale. L'indagine di Vulnerability Assessment effettuata da MGALabs si basa su una metodicità e una scrupolosità sviluppate anche grazie all'esperienza maturata operando su numerosi progetti distribuiti.</p>
    <p>
    ",
    "{static}/images/home.png",
    "Alt Text")
}}


{{ row("",
    "<p>MGALabs offre servizi professionali destinati ad accompagnare nel proprio percorso tecnologico qualsiasi azienda già avviata o soluzioni mirate a sviluppo.</p>",
    "",
    "")
}}

{{ row("Row Title",
    "
    <p>Un'attività di Penetration Testing è un processo operativo per la valutazione 
della reale sicurezza cibernetica di un sistema informativo, inteso come 
applicazioni, infrastruttura informatica, rete o insieme di esse.</p>

<p>La sua finalità è identificare le vulnerabilità realmente sfruttabili da un attaccante 
tramite lo svolgimento di un'attività cibernetica offensiva che vede l'utilizzo di 
reali tattiche, tecniche e procedure (TTP) di attacco in modo da ottenere una 
simulazione pressoché realistica e atta ad individuare i rischi di un attacco nello 
spazio cibernetico.</p>

<p>L'attacco esclude tutte quelle tecniche offensive, l'utilizzo di vulnerabilità o di 
strumenti che possono causare un disservizio, anche temporaneo, all'obiettivo 
dell'attività. L'analisi è condotta dal punto di vista di un potenziale attaccante, 
impersonato da un ethical hacker, e consiste nell'individuazione e sfruttamento 
delle vulnerabilità, tramite tecniche di exploiting e persistenza nei sistemi, al fine 
di ottenere l'accesso a uno o più sistemi e alle informazioni da esso contenute.</p>    
    ",
    "{static}/images/forensics.png",
    "Alt Text")
}}