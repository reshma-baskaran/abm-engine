# ABM Engine Outreach — Deterministic Signal Library

**Use case:** ABM signal scoring for ABM Engine professional services (voice agents, conversational AI, contact-center automation, agentic workflows, AI-led CX automation).

**Scope:** All signals consolidated from sub-industry research and reclassified as **deterministic** for the outreach tool. Organized by industry → sub-industry → category.

**Conventions:**
- Every signal includes: `key`, label, category, search query template (where available), rationale, and weight/confidence (where available).
- Variables: `{{company_name}}`, `{{company_domain}}`, `{{ticker}}`, ATS slugs.
- Weights are preserved on whichever scale the source used (0.5–2.0 in some libraries, 1–5 or 1–10 in others). Treat as relative-priority within a sub-industry.

---

# INDUSTRY: RETAIL

---

## Sub-Industry: Auto Parts Retail (US)

**Universe:** AutoZone, Advance Auto Parts, O'Reilly Automotive, Genuine Parts Company / NAPA, Pep Boys, CarParts.com, RockAuto, US Auto Parts Network, AutoNation Mobile Service, Monro, Driven Brands.

### Hiring

- **`hiring_conversational_voice_ai_role`** — Open role for Conversational/Voice AI engineer or designer. Weight 1.95 / Conf 4. Query: `("{{company_name}}" jobs OR careers) ("conversational AI" OR "voice AI" OR "voice agent" OR "dialog systems" OR "NLU engineer") (site:linkedin.com/jobs OR site:greenhouse.io OR site:lever.co OR site:myworkdayjobs.com)`. *Rationale:* Hiring conv/voice AI talent = explicitly building same capability ABM Engine sells.
- **`hiring_contact_center_modernization`** — Open roles for contact center / BDC / CX transformation leadership. Weight 1.55 / Conf 3. Query: `"{{company_name}}" ("contact center" OR "call center" OR "customer care" OR "BDC manager" OR "customer experience transformation" OR "digital servicing") (manager OR director OR VP OR "head of") (site:linkedin.com/jobs OR site:indeed.com OR site:greenhouse.io)`. *Rationale:* New CX/contact-center leadership = budget re-baselining, voice/CCaaS-AI evaluation window.
- **`hiring_ml_data_science_volume`** — Volume of open ML / Data Science / MLOps requisitions. Weight 1.20 / Conf 3. Query: `"{{company_name}}" ("machine learning engineer" OR "data scientist" OR "MLOps" OR "ML platform" OR "AI engineer" OR "applied scientist") (site:linkedin.com/jobs OR site:greenhouse.io)`. *Rationale:* Standing ML/DS bench means org can co-build with ABM Engine services.
- **`hiring_ecommerce_personalization_search`** — E-commerce / catalog search / personalization roles open. Weight 1.15 / Conf 3. Query: `"{{company_name}}" ("search relevance" OR "personalization" OR "product discovery" OR "catalog" OR "fitment" OR "recommendations engine") (engineer OR scientist OR manager)`. *Rationale:* Parts retail's #1 problem is fitment; AI search hiring = data layer for agentic workflows.
- **`hiring_cdp_data_platform_roles`** — CDP, data platform, or "AI-ready data" engineering roles. Weight 1.10 / Conf 3. Query: `"{{company_name}}" ("customer data platform" OR "CDP" OR "Snowflake" OR "Databricks" OR "data platform" OR "data governance" OR "Alation" OR "Collibra") (engineer OR architect OR manager)`. *Rationale:* Governed data layer is precondition for safe agentic deployment.

### Tech Stack

- **`tech_stack_existing_voice_cx_vendor`** — Existing voice AI / CCaaS vendor deployed. Weight 1.50 / Conf 3. Query: `"{{company_name}}" ("Five9" OR "NICE CXone" OR "Genesys Cloud" OR "Talkdesk" OR "Amazon Connect" OR "Twilio Flex" OR "Webex Contact Center" OR "Cresta" OR "ASAPP" OR "Cognigy" OR "Kore.ai" OR "Replicant" OR "PolyAI")`. *Rationale:* Legacy stack = green light for upgrade; modern stack = sell agentic workflows above the platform.
- **`tech_stack_palantir_foundry`** — Palantir Foundry or similar AI-ops platform deployment. Weight 1.65 / Conf 4. Query: `"{{company_name}}" ("Palantir" OR "Foundry" OR "C3.ai" OR "Databricks" OR "DataRobot") (deployment OR partnership OR earnings OR implemented)`. *Rationale:* Org comfortable with outcome-priced services-heavy AI software (AAP's Palantir deployment is canonical).

### Partnership

- **`tech_stack_hyperscaler_ai_partnership`** — Public hyperscaler AI partnership announcement. Weight 1.90 / Conf 4. Query: `"{{company_name}}" ("Google Cloud" OR "Gemini Enterprise" OR "Amazon Bedrock" OR "AWS" OR "Azure OpenAI" OR "Vertex AI") (partnership OR announces OR migration OR agentic OR "AI")`. *Rationale:* Anchors 2-3 year AI roadmap with committed budget; pro-services partners selected within 1-2 quarters.
- **`partnership_systems_integrator`** — Engagement with major SI / consultancy on digital or AI. Weight 0.85 / Conf 2. Query: `"{{company_name}}" ("Accenture" OR "Deloitte" OR "Slalom" OR "Publicis Sapient" OR "EPAM" OR "Cognizant" OR "Capgemini" OR "TCS" OR "Infosys") (AI OR digital OR transformation OR partnership)`.

### Strategic

- **`strategic_earnings_call_ai_mentions`** — Earnings-call AI / automation / GenAI mention frequency. Weight 1.60 / Conf 3. Query: `"{{company_name}}" ("earnings call" OR "transcript" OR "10-Q" OR "10-K") ("artificial intelligence" OR "generative AI" OR "automation" OR "AI agent") site:seekingalpha.com OR site:fool.com OR site:investing.com OR site:sec.gov`. *Rationale:* Rising AI rhetoric = CEO publicly committed and being measured.
- **`strategic_10k_technology_capex`** — 10-K / 10-Q technology and digital capex disclosure. Weight 0.95 / Conf 3. Query: `"{{company_name}}" 10-K ("technology investment" OR "information technology" OR "digital" OR "e-commerce platform" OR "system modernization") site:sec.gov`. *Rationale:* YoY tech-capex bump = clearest financial indicator dry powder exists.
- **`ev_transition_strategy_disclosure`** — EV-mix and EV-parts strategy disclosure. Weight 0.50 / Conf 2. Query: `"{{company_name}}" ("electric vehicle" OR "EV" OR "battery" OR "hybrid") (strategy OR "parts mix" OR earnings) site:sec.gov`.

### Leadership

- **`leadership_new_cto_cio_18mo`** — New CTO/CIO/CDO/Chief AI Officer hired in last 18 months. Weight 2.00 / Conf 4. Query: `"{{company_name}}" ("appoints" OR "names" OR "joins as" OR "hires") ("chief technology officer" OR "CTO" OR "chief information officer" OR "CIO" OR "chief digital officer" OR "CDO" OR "chief AI officer" OR "chief data officer" OR "VP technology" OR "EVP technology")`. *Rationale:* New tech leadership ALWAYS rebuilds vendor stack within 12 months — highest-conversion signal.
- **`leadership_cx_or_commercial_exec_change`** — New Chief Customer / Commercial / E-commerce officer in last 18 months. Weight 1.80 / Conf 4. Query: `"{{company_name}}" ("chief customer officer" OR "chief commercial officer" OR "chief e-commerce officer" OR "VP customer experience" OR "head of digital") ("appoints" OR "names" OR "joins")`. *Rationale:* CX-side exec changes reset call-center, BDC, commercial-desk vendor stacks — owns voice/CX-automation buys.
- **`leadership_linkedin_ai_thought_leadership`** — Exec LinkedIn posts on AI / agentic / GenAI in last 6 months. Weight 1.05 / Conf 3. Query: `"{{company_name}}" (CEO OR CTO OR CIO OR CDO) ("artificial intelligence" OR "generative AI" OR "agentic" OR "AI agent") site:linkedin.com`.

### CX Pain

- **`cx_pain_complaints_call_wait_times`** — Public complaints about call wait, customer service, or commercial desk service. Weight 1.45 / Conf 3. Query: `"{{company_name}}" ("on hold" OR "wait time" OR "no one answered" OR "horrible customer service" OR "commercial desk" OR "wrong part" OR "could not reach") (site:reddit.com OR site:trustpilot.com OR site:bbb.org OR site:consumeraffairs.com OR site:pissedconsumer.com)`. *Rationale:* This is the literal problem statement ABM Engine solves.
- **`cx_pain_mobile_app_reviews`** — App Store / Play Store recent low ratings on support functionality. Weight 0.90 / Conf 3.
- **`cx_pain_reddit_subreddit_complaints`** — Volume of negative threads in retailer-specific subreddit. Weight 0.75 / Conf 2.
- **`cx_pain_glassdoor_call_center_understaffing`** — Glassdoor reviews citing understaffed BDC/commercial/customer-care. Weight 0.85 / Conf 2. *Rationale:* Frontline staff publicly saying they can't keep up = finance is actively looking for headcount-avoidance ROI.

### Volume

- **`volume_store_count_and_commercial_program`** — Store count, commercial program size, and YoY growth. Weight 1.10 / Conf 3. Query: `"{{company_name}}" ("store count" OR "commercial sales" OR "Pro program" OR "DIFM" OR "professional installer") (10-K OR investor OR earnings)`.
- **`volume_call_center_fte_estimate`** — Estimated call-center / customer-care headcount via LinkedIn. Weight 1.00 / Conf 2. *Rationale:* Headcount × loaded cost = ROI denominator.

### AI Initiatives

- **`ai_initiative_press_release`** — Press release announcing AI pilot, launch, or partnership. Weight 2.00 / Conf 4. Query: `"{{company_name}}" ("announces" OR "launches" OR "pilots" OR "partners with") ("AI" OR "artificial intelligence" OR "generative AI" OR "voice agent" OR "chatbot" OR "agentic")`. *Rationale:* Cleanest single signal — proof org has crossed into production AI buying.
- **`ai_initiative_conference_appearance`** — Exec speaking on AI at industry/AI conference. Weight 1.30 / Conf 3. Query: `"{{company_name}}" (speaker OR session OR panel OR keynote) (AAPEX OR SEMA OR NRF OR Shoptalk OR "Google Cloud Next" OR "AWS re:Invent" OR "Snowflake Summit" OR "Databricks") (AI OR data)`.
- **`ai_initiative_internal_llm_or_copilot`** — Internal employee-facing LLM / copilot deployed. Weight 1.40 / Conf 3. Query: `"{{company_name}}" ("internal AI" OR "AI assistant" OR "employee copilot" OR "internal ChatGPT" OR "ChatGPC" OR "AI center of excellence")`.

### Digital Maturity

- **`digital_maturity_chat_widget_present`** — Site has live chat / chatbot widget on customer or pro site. Weight 1.20 / Conf 4. Query: `site:{{company_name}}.com ("chat" OR "live chat" OR "ask us" OR "virtual assistant") -inurl:investor`.
- **`digital_maturity_fitment_vin_search_sophistication`** — VIN/license-plate/fitment search sophistication. Weight 0.80 / Conf 3.
- **`digital_maturity_mobile_app_cadence`** — Mobile app update cadence and rating. Weight 0.65 / Conf 3. Query: `"{{company_name}}" app site:apps.apple.com OR site:play.google.com`.

### Funding

- **`funding_activist_investor_turnaround`** — Activist investor pressure with digital/tech modernization mandate. Weight 1.50 / Conf 4. Query: `"{{company_name}}" ("activist investor" OR "Third Point" OR "H Partners" OR "Legion Partners" OR "Starboard" OR "Engine Capital" OR "Saddle Point") (board OR turnaround OR cooperation agreement)`. *Rationale:* Activist boards force transformation within 12-24 months (AAP case).
- **`funding_restructuring_with_tech_emphasis`** — Restructuring plan that names technology / digital pillars. Weight 1.20 / Conf 3. Query: `"{{company_name}}" ("restructuring" OR "turnaround plan" OR "strategic plan" OR "three-year plan") ("technology" OR "digital" OR "AI" OR "automation")`.

### Regulatory

- **`regulatory_repair_act_engagement`** — Engagement with REPAIR Act / Right-to-Repair advocacy. Weight 0.55 / Conf 2. Query: `"{{company_name}}" ("REPAIR Act" OR "right to repair" OR "Auto Care Association" OR "MEMA" OR "CAR Coalition") (testimony OR statement OR support)`.

---

## Sub-Industry: E-commerce & D2C (US)

**Scope:** US D2C and e-commerce brands across all verticals (Shopify Plus/Hydrogen, Klaviyo, headless commerce ecosystem). 62 signals.

### Hiring

- **`open_ml_engineering_roles`** — Open ML/AI Engineering Job Postings. Weight 1.80 / Conf 4. Query: `site:boards.greenhouse.io "{{company_name}}" ("machine learning" OR "ML engineer" OR "applied scientist") OR site:jobs.lever.co "{{company_name}}" ("ML" OR "AI engineer") OR site:jobs.ashbyhq.com "{{company_name}}" ("machine learning" OR AI)`. Detection: ≥1 active posting in last 90 days. *Rationale:* Most direct proxy for committed AI investment.
- **`volume_ai_roles_open`** — ≥3 Concurrent AI Roles Open. Weight 2.00 / Conf 5. Programmatic via ATS APIs. *Rationale:* 3+ concurrent roles = funded team build, not experiment.
- **`ai_leadership_role_posted`** — VP/Head/Director of AI Role Posted. Weight 1.90 / Conf 5. Query: `site:boards.greenhouse.io OR site:jobs.lever.co OR site:jobs.ashbyhq.com "{{company_name}}" ("Head of AI" OR "VP AI" OR "VP Machine Learning" OR "Director, AI" OR "Chief AI Officer")`.
- **`personalization_engineer_role`** — Personalization / Recommendation Systems Engineer. Weight 1.50 / Conf 4. Query: `site:boards.greenhouse.io "{{company_name}}" ("personalization engineer" OR "recommendation systems" OR "recsys" OR "search relevance")`. *Rationale:* Core D2C unit-economics revenue lever.
- **`computer_vision_for_retail_role`** — CV Engineer (Visual Search / Try-On). Weight 1.40 / Conf 4. Query: `site:boards.greenhouse.io OR site:jobs.lever.co "{{company_name}}" ("computer vision" OR "visual search" OR "virtual try-on" OR "AR engineer")`.
- **`pricing_demand_forecasting_role`** — Pricing/Demand Forecasting Algorithm Engineer. Weight 1.30 / Conf 4. Query: `"{{company_name}}" ("pricing algorithm" OR "demand forecasting" OR "inventory optimization" OR "markdown optimization") (engineer OR scientist)`.
- **`conversational_ai_role`** — Conversational AI / LLM Engineer. Weight 1.60 / Conf 4. Query: `"{{company_name}}" ("LLM engineer" OR "conversational AI" OR "prompt engineer" OR "GenAI engineer") site:greenhouse.io OR site:lever.co OR site:ashbyhq.com`.
- **`mlops_data_platform_role`** — MLOps / Data Platform Engineer. Weight 1.20 / Conf 3. Query: `"{{company_name}}" ("MLOps" OR "ML platform" OR "data platform engineer" OR "feature store")`.
- **`analytics_engineer_with_ai_jd`** — Analytics Engineer JD Mentions AI/ML. Weight 0.80 / Conf 3.
- **`geographic_ai_hub`** — Multi-City AI Hiring Footprint (≥2 distinct metros). Weight 1.10 / Conf 3.
- **`ai_internship_program`** — AI/ML Internship Postings. Weight 0.90 / Conf 3.
- **`ai_governance_role`** — AI Ethics / Governance Role. Weight 1.30 / Conf 4. Query: `"{{company_name}}" ("responsible AI" OR "AI governance" OR "AI ethics" OR "AI risk") site:greenhouse.io OR site:lever.co`.

### Funding & Financial

- **`funding_round_mentions_ai`** — Recent Funding Round Cites AI. Weight 1.50 / Conf 4. Query: `"{{company_name}}" ("Series A" OR "Series B" OR "Series C" OR "Series D" OR "raised") ("AI" OR "artificial intelligence" OR "machine learning") site:techcrunch.com OR site:businesswire.com OR site:prnewswire.com`.
- **`10k_ai_mentions_count`** — 10-K AI Mention Count (≥5 sentences). Weight 1.40 / Conf 4. Query: `site:sec.gov "{{company_name}}" 10-K "artificial intelligence"`. Bonus weight if AI in Business or MD&A (not just Risk Factors).
- **`10q_quarterly_ai_uptick`** — 10-Q AI Mention Growth QoQ (monotonic increase across 3 quarters). Weight 1.10 / Conf 3.
- **`earnings_call_ai_mentions`** — Earnings Call AI Mentions (≥3 executive mentions across last 2 calls). Weight 1.30 / Conf 4.
- **`investor_day_ai_track`** — Investor Day Has AI Track. Weight 1.20 / Conf 3.
- **`annual_letter_ai_mention`** — Shareholder Letter Mentions AI. Weight 1.00 / Conf 3.
- **`s1_ai_strategy_section`** — S-1/F-1 AI Strategy Section. Weight 1.40 / Conf 4.
- **`ai_capex_disclosure`** — Disclosed AI/Cloud Capex. Weight 1.20 / Conf 3.

### Tech Stack

- **`algolia_neuralsearch_detected`** — Algolia + NeuralSearch on Storefront. Weight 1.50 / Conf 4. BuiltWith + DOM scan for `algolia.com` + `neuralsearch` or `@algolia/recommend`.
- **`constructor_io_detected`** — Constructor.io AI Product Discovery. Weight 1.70 / Conf 5. BuiltWith + DOM check for `cnstrc.com` or `constructorio`. *Rationale:* AI-native; high-confidence (Sephora, Backcountry, Bonobos).
- **`bloomreach_loomi_detected`** — Bloomreach Discovery / Loomi AI. Weight 1.50 / Conf 4. BuiltWith for `bloomreach.com`; DOM for `brsuggest`/`brapi`.
- **`coveo_detected`** — Coveo Search. Weight 1.30 / Conf 4.
- **`klevu_searchspring_detected`** — Klevu or Searchspring AI Search. Weight 1.10 / Conf 3. DOM for `klevu.com` or `searchspring.io`.
- **`klaviyo_with_ai_features`** — Klaviyo Active + AI Features Enabled. Weight 1.20 / Conf 4. BuiltWith for `klaviyo.com` + customer story or JD mentions Klaviyo AI/Composer/Customer Agent.
- **`shopify_magic_sidekick_usage`** — Shopify Magic / Sidekick References. Weight 0.90 / Conf 3.
- **`shopify_hydrogen_headless`** — Shopify Hydrogen / Headless Architecture. Weight 1.30 / Conf 4. Check response headers for `oxygen-`; BuiltWith for "Hydrogen"; DOM for `@shopify/hydrogen-react`.
- **`commercetools_detected`** — commercetools Composable Commerce. Weight 1.20 / Conf 3.
- **`nosto_personalization_detected`** — Nosto Personalization Script. Weight 1.20 / Conf 4.
- **`dynamic_yield_detected`** — Dynamic Yield (Mastercard) Script. Weight 1.40 / Conf 4. DOM for `dynamicyield.com` / `dy_api`.
- **`rebuy_smartcart`** — Rebuy AI Smart Cart on Shopify. Weight 0.80 / Conf 3.
- **`gorgias_ai_agent`** — Gorgias AI Agent / Helpdesk. Weight 1.10 / Conf 3.
- **`ada_intercom_fin_kustomer`** — Enterprise Conversational AI (Ada / Intercom Fin / Kustomer). Weight 1.30 / Conf 4.
- **`pinecone_weaviate_qdrant_disclosed`** — Vector DB in Job Descriptions. Weight 1.60 / Conf 5. Query: `"{{company_name}}" ("Pinecone" OR "Weaviate" OR "Qdrant" OR "Chroma" OR "Milvus") site:greenhouse.io OR site:lever.co OR site:ashbyhq.com`. *Rationale:* Production RAG / semantic search workloads.
- **`llm_vendor_in_jd`** — OpenAI/Anthropic/Bedrock/Vertex Named in JD. Weight 1.50 / Conf 4.
- **`databricks_customer`** — Databricks Customer Story or Job Mention. Weight 1.40 / Conf 4. Query: `"{{company_name}}" site:databricks.com/customers OR site:databricks.com/blog`.
- **`snowflake_customer`** — Snowflake Customer / Retail Data Cloud. Weight 1.30 / Conf 4.
- **`sagemaker_vertex_in_jd`** — SageMaker / Vertex AI / Azure ML in JD. Weight 1.10 / Conf 3.
- **`mlops_tooling_disclosed`** — W&B / MLflow / Comet / Tecton in JD. Weight 1.00 / Conf 3.
- **`kafka_kinesis_realtime`** — Real-Time Data Infra (Kafka/Kinesis) in JD. Weight 0.80 / Conf 3.
- **`visual_search_vendor_detected`** — Syte / ViSenze / Vue.ai Visual Search. Weight 1.50 / Conf 4.
- **`marketing_ai_persado_phrasee`** — Persado / Phrasee / Movable Ink AI. Weight 1.10 / Conf 3.
- **`engineering_blog_ai_post`** — Engineering Blog Post on AI/ML in last 24 mo. Weight 1.40 / Conf 4. Query: `site:{{company_domain}} ("machine learning" OR "deep learning" OR "LLM" OR "recommendation system") inurl:engineering OR inurl:tech OR inurl:blog`.
- **`github_ai_repos`** — Public GitHub Repos in AI/ML. Weight 1.20 / Conf 4.

### Leadership

- **`chief_ai_officer_appointed`** — Chief AI Officer Appointment in last 18 mo. Weight 2.00 / Conf 5. Query: `"{{company_name}}" ("Chief AI Officer" OR "Chief AI and Technology Officer" OR "Chief Data and AI Officer") (appointed OR named OR hires)`.
- **`chief_data_officer_appointed`** — Chief Data Officer / VP Data. Weight 1.50 / Conf 4.
- **`head_of_ai_ml_hired`** — Head of AI / VP ML Hired. Weight 1.70 / Conf 4.
- **`faang_ai_hire`** — Recent Hire from FAANG/OpenAI/Anthropic AI team. Weight 1.40 / Conf 4.
- **`board_member_ai_expertise`** — Board Addition with AI Background. Weight 1.30 / Conf 3.
- **`linkedin_ai_leader_announcement`** — LinkedIn AI-Hire Announcement by CEO. Weight 1.10 / Conf 3.
- **`new_ai_focused_org_unit`** — New AI/ML Org Unit Announced (CoE / Lab). Weight 1.30 / Conf 3.

### Strategic Statements

- **`ceo_ai_interview_podcast`** — CEO AI Strategy in Interview/Podcast. Weight 1.20 / Conf 3.
- **`nrf_shoptalk_keynote_ai`** — NRF / Shoptalk / eTail Keynote on AI. Weight 1.50 / Conf 4.
- **`aws_reinvent_gcp_next_customer_session`** — Cloud Conference Customer Spotlight (re:Invent / Next / Ignite / Snowflake Summit / Data + AI Summit). Weight 1.40 / Conf 4.
- **`published_case_study_ai_vendor`** — Published Case Study by Tier-1 AI Vendor. Weight 1.80 / Conf 5. Query: `"{{company_name}}" (site:openai.com/customer-stories OR site:anthropic.com OR site:pinecone.io OR site:databricks.com/customers OR site:snowflake.com/customers OR site:algolia.com/customers OR site:constructor.com)`.
- **`press_release_ai_initiative`** — Brand-Issued AI Initiative Press Release. Weight 1.40 / Conf 4.
- **`earnings_call_ai_keyword_count`** — ≥10 AI keyword mentions per call, rising QoQ. Weight 1.30 / Conf 4.
- **`annual_report_ai_section`** — Annual Report Dedicated AI Section. Weight 1.30 / Conf 4.

### Partnerships

- **`microsoft_openai_partnership`** — Microsoft / OpenAI / Azure OpenAI Partnership. Weight 1.70 / Conf 5.
- **`anthropic_claude_partnership`** — Anthropic / Claude Deployment. Weight 1.60 / Conf 4.
- **`aws_bedrock_partnership`** — AWS Bedrock / SageMaker Customer Spotlight. Weight 1.30 / Conf 4.
- **`google_cloud_vertex_partnership`** — Google Cloud Vertex AI Customer. Weight 1.30 / Conf 4.
- **`salesforce_einstein_agentforce`** — Salesforce Einstein / Agentforce / Commerce Cloud AI. Weight 1.20 / Conf 3.
- **`adobe_sensei_firefly_partnership`** — Adobe Sensei / Firefly Customer. Weight 1.10 / Conf 3.
- **`chatgpt_instant_checkout_participant`** — ChatGPT Instant Checkout / Agentic Commerce Protocol Merchant. Weight 1.80 / Conf 5. Query: `"{{company_name}}" ("Instant Checkout" OR "Agentic Commerce Protocol" OR "ChatGPT shopping")`. Sources: openai.com/index/buy-it-in-chatgpt.
- **`google_ucp_gemini_partner`** — Google Universal Commerce Protocol / Gemini Shopping. Weight 1.60 / Conf 4.
- **`perplexity_buy_with_pro`** — Perplexity Buy-with-Pro Merchant. Weight 1.30 / Conf 3.
- **`shopify_plus_ai_co_marketing`** — Shopify Plus AI Co-Marketed Launch. Weight 1.10 / Conf 3.

### Product & UX (Storefront-Visible)

- **`ai_chatbot_widget_present`** — AI Chatbot Widget on Storefront. Weight 1.20 / Conf 4. DOM scan for `ada.support`, `intercomcdn`, `gorgias.chat`, `kustomerapp.com`, `tidio.com`, `drift.com`, `zowie.ai`, `tolstoy`.
- **`semantic_search_endpoint`** — Semantic/Natural-Language Search Visible. Weight 1.50 / Conf 4. Network inspection for `algolia.com/recommend`, `cnstrc.com`, `bloomreach`, `coveo` endpoints.
- **`visual_search_camera_button`** — "Search by Photo" / Camera-Icon Search. Weight 1.60 / Conf 4. DOM scan for image-upload search or `syte.ai`, `visenze.com`, `vue.ai`, `pixyle`.
- **`personalized_homepage_blocks`** — "Recommended for You" Homepage Sections + vendor script. Weight 0.80 / Conf 3.
- **`virtual_try_on_ar`** — Virtual Try-On / AR Feature. Weight 1.50 / Conf 4. DOM/URL for `try-on`, `perfectcorp.com`, `modiface.com`, `8thwall`.
- **`ai_generated_imagery_labels`** — "AI-Generated"/"Powered by AI" Labels on Site. Weight 1.00 / Conf 3.
- **`conversational_shopping_assistant`** — Branded Conversational Shopping Assistant (klaviyo customer agent, rep.ai, tolstoy AI shopper, gorgias AI agent). Weight 1.40 / Conf 4.
- **`ai_product_descriptions_disclosed`** — Disclosed AI-Generated Product Copy. Weight 0.70 / Conf 3.
- **`dynamic_pricing_observed`** — ≥3 Price Changes Observed Within 14 Days. Weight 0.80 / Conf 3.

### Infrastructure

- **`heavy_cloud_ml_footprint_jd`** — Cloud + ML Skills (K8s/Ray/Triton + model serving) in JD. Weight 1.10 / Conf 3.
- **`data_warehouse_disclosed`** — Snowflake/Databricks/BigQuery in ≥2 JDs. Weight 1.10 / Conf 3.
- **`gpu_compute_disclosure`** — GPU / A100/H100 / NVIDIA Mentions. Weight 1.20 / Conf 3.
- **`engineering_blog_ml_infra_post`** — ML Infrastructure Blog Post in last 24 mo. Weight 1.30 / Conf 4.
- **`streaming_data_infra_jd`** — Kafka/Kinesis/Flink in JD. Weight 0.80 / Conf 3.
- **`vector_db_in_engineering_blog`** — Vector DB Mention in Engineering Blog. Weight 1.50 / Conf 4.

### Compliance & Governance

- **`ai_principles_page_published`** — Published Responsible AI / AI Principles Page. Weight 1.40 / Conf 4.
- **`privacy_policy_ai_clauses`** — Privacy Policy Mentions AI/ML Data Use. Weight 0.80 / Conf 3.
- **`ai_governance_role_open`** — Open Role: AI Governance / Responsible AI. Weight 1.30 / Conf 4.
- **`partnership_on_ai_member`** — Industry AI Body Membership (Partnership on AI / MLCommons / AI Alliance). Weight 0.70 / Conf 3.

### M&A

- **`acquired_ai_startup`** — Acquired an AI Startup in last 24 mo. Weight 1.90 / Conf 5.
- **`acquihire_ai_team`** — Acqui-Hire of AI Team. Weight 1.50 / Conf 4.
- **`strategic_investment_in_ai_company`** — Strategic Investment in AI Company. Weight 1.20 / Conf 3.

### Operational

- **`patent_filing_ml_recommendation`** — USPTO Patent Filing on AI/ML in last 36 mo. Weight 1.30 / Conf 4.
- **`employee_arxiv_publication`** — Employee arXiv / NeurIPS / KDD Publication. Weight 1.40 / Conf 4.
- **`ai_conference_sponsorship`** — AI/ML Conference Sponsorship (NeurIPS/KDD/ICML/MLOps World). Weight 1.00 / Conf 3.
- **`hackathon_ai_themed`** — AI-Themed Hackathon Hosted. Weight 0.80 / Conf 3.
- **`university_ai_partnership`** — Stanford HAI / MIT CSAIL / CMU / Berkeley AI Research Partnership. Weight 1.10 / Conf 3.
- **`product_launch_ai_branded`** — AI-Branded Product Launch Press Release. Weight 1.20 / Conf 3.
- **`careers_page_ai_section`** — Dedicated "AI at {{Company}}" Careers Section. Weight 1.30 / Conf 4.

---

## Sub-Industry: Grocery & Food Retail (US)

**Universe:** Walmart, Kroger, Albertsons, Ahold Delhaize, Amazon/Whole Foods, Publix, H-E-B, Aldi US, Dollar General, Hy-Vee, Wakefern, Tops, Price Chopper, Stater Bros., Sprouts, Grocery Outlet, BJ's, SpartanNash, Cub/UNFI, Wegmans, etc.

### Hiring

- **`hiring_ai_ml_engineer`** — Open postings: "ML Engineer," "AI Engineer," "ML Platform," "MLOps," "Applied Scientist," "Generative AI Engineer," "LLM Engineer." *High confidence:* ≥3 active senior (L5+/Staff/Principal) reqs at HQ.
- **`hiring_conv_voice_ai`** — Postings: "conversational AI" OR "voice AI" OR "chatbot" OR "IVR" OR "speech recognition" OR "NLU" OR "Dialogflow" OR "Lex" OR "Cognigy" OR "Cresta" OR "Replicant." *Rationale:* Explicit declaration of conversational AI program.
- **`hiring_contact_center_modernization`** — "Contact Center" OR "Customer Care" + "modernization" / "transformation" / "cloud" / "CCaaS," plus Genesys / NICE CXone / Five9 / Talkdesk / Amazon Connect / Cisco Webex Contact Center / RingCentral stack mentions. *Rationale:* Re-platforming projects almost always carry AI workstreams.
- **`hiring_data_science_team`** — Multiple postings within 90 days for "Data Scientist," "Data Engineer," "Analytics Engineer," "Snowflake," "Databricks," "BigQuery," "Vertex AI," "SageMaker." *High confidence:* ≥5 reqs incl. leadership role.
- **`hiring_cx_technology_leader`** — Posting/appointment with "VP/Director of Customer Experience" OR "Head of Digital CX" OR "VP Contact Center" OR "Head of Customer Care Technology."
- **`hiring_automation_role`** — "RPA Developer," "Process Automation," "Intelligent Automation," "UiPath," "Automation Anywhere," "Workflow Engineer," "Agentic Automation."
- **`hiring_velocity`** — Total AI/data/automation-related job postings normalized by headcount/store count over rolling 90 days. *Rationale:* Going from 0 → 8 such postings in a quarter is materially more ripe than 3 stable.

### Leadership

- **`new_cdo_caio_cto_appointment`** — Press release, LinkedIn, 8-K, or proxy filing showing CAIO/CDO/CIO/EVP Tech/VP-SVP AI/Transformation appointment within 12 months. *High confidence:* title contains "AI" or "Digital Transformation," reports to CEO.
- **`board_level_ai_governance`** — 10-K/proxy mentions of board committee for AI/tech risk; director with AI background; ESG report on AI ethics.
- **`ceo_personal_ai_commitment`** — CEO personally appeared at AI-themed events (NRF Big Show, Groceryshop AI panels, Microsoft/Google retail keynotes) within 12 months.

### Strategic / Leadership

- **`exec_thought_leadership_ai`** — CEO/CIO/CDO LinkedIn posts, conference keynotes (NRF, Groceryshop, FMI Midwinter), press quotes over rolling 6 months mentioning "agentic AI," "we are exploring," "pilots underway," "customer journey," "associate productivity," "frictionless."

### Technology Stack

- **`hyperscaler_partnership`** — Press release / vendor case study confirming Google Cloud (Vertex AI, Gemini Enterprise), AWS (Bedrock, SageMaker, Connect, Q), or Microsoft Azure (OpenAI Service, Copilot Studio, Dynamics 365 Contact Center) relationship. *High confidence:* named CX/conversational AI use case.
- **`ccaas_platform_in_use`** — BuiltWith / HG Insights / ZoomInfo / company press indicating Genesys Cloud CX, NICE CXone, Five9, Talkdesk, Amazon Connect, Cisco UCCE, Avaya, RingCentral.
- **`legacy_telephony_indicators`** — Job postings referencing on-prem Avaya, Cisco UCM, NEC, Mitel, ShoreTel, legacy IVR, AS/400-era infra. *Rationale:* Prime cloud + AI overhaul candidate.
- **`crm_platform`** — Salesforce / Microsoft Dynamics 365 / SAP CX / Oracle CX / HubSpot deployment with Service Cloud / Customer Service module.
- **`data_platform_modernization`** — Snowflake, Databricks, BigQuery, Redshift, Confluent, dbt, or "unified customer data platform" mentions.
- **`self_checkout_smart_cart`** — Press/analyst report on Toshiba/NCR/Fujitsu self-checkout expansion, Instacart Caper Carts, AiFi, Grabango, Trigo, AWM Smart Shelf deployment.
- **`ecommerce_platform_modernization`** — Migration to headless commerce / proprietary platform / partnership with Mirakl, commercetools, BigCommerce, Salesforce Commerce, Adobe Commerce, Instacart Storefront Pro.
- **`api_integration_modernization`** — Engineering blog posts, GitHub, conference talks: "API-first," "microservices migration," "event-driven architecture," "MACH stack."

### Strategic (Earnings, Filings, Investor Days)

- **`earnings_call_ai_mentions`** — Count of "AI," "artificial intelligence," "machine learning," "generative AI," "agentic AI," "automation," "digital transformation," "personalization at scale" in last 4 earnings transcripts. *High confidence:* ≥5 mentions, named specific use cases, YoY increase.
- **`10k_technology_investment_language`** — 10-K Risk Factors, MD&A, Capital Expenditures sections referencing tech investment, digital transformation costs, "business transformation costs" line items, AI-related risk disclosures.
- **`investor_day_ai_strategy`** — Dedicated AI/technology slides or sessions at investor/capital markets days; quantified ROI targets.
- **`agentic_commerce_priority_signal`** — Explicit "agentic commerce," "AI shopping assistant," "conversational commerce" mentions + integration with OpenAI/ChatGPT, Perplexity, Google Gemini, Microsoft Copilot, Anthropic Claude as partner.
- **`margin_pressure_language`** — Earnings/10-K mentions of "margin compression," "productivity initiatives," "labor cost pressure," "competitive intensity," "Save for Our Customer."
- **`customer_experience_north_star`** — Repeated framing of "customer for life," "customer-obsessed," "white-glove experience," "frictionless," "personalized at scale" across CEO letter + investor day + 10-K.

### CX Pain

- **`low_trustpilot_rating`** — Trustpilot/Sitejabber/BBB/ConsumerAffairs rating <2.5 stars with >500 reviews.
- **`cx_complaint_themes`** — Theme clusters on Trustpilot/BBB/Reddit/Google Reviews/app stores: long checkout wait, deli/pharmacy abandonment, broken self-checkout/lockup, digital-coupon failures, delivery substitution errors, unreachable customer service, IVR frustration, language access.
- **`app_store_review_velocity_decline`** — Rolling 30-day iOS/Google Play rating drop OR rising volume of 1-star reviews (app crashes, login failures, checkout failure).
- **`social_complaint_volume`** — X/Twitter/Reddit/Facebook complaint volume spikes during seasonal surges (Thanksgiving, holidays, hurricanes).
- **`bbb_complaint_count`** — BBB cumulative complaint count growth YoY. *High confidence:* >25% growth with >100 absolute volume.
- **`glassdoor_call_center_sentiment`** — Glassdoor/Indeed reviews from call-center agent roles citing high call volume, mandatory overtime, abusive callers, outdated tools.

### Operational & Volume

- **`store_count`** — Total US store count from 10-K. *High confidence:* >300 stores.
- **`ecommerce_volume_growth`** — YoY online sales growth; absolute digital sales penetration.
- **`delivery_partner_density`** — Number of named delivery partners (Instacart, DoorDash, Uber Eats, Shipt, Amazon Flex, 1st-party fleet).
- **`call_center_size_indicator`** — Triangulated from LinkedIn employee count (Customer Service Rep / Customer Care / Contact Center Agent titles), BPO contract press (Foundever, Teleperformance, TTEC, Concentrix, Alorica), job-board hiring volume.
- **`seasonal_call_surge_indicator`** — News of call-handling failures or extended wait times around Thanksgiving/Christmas/back-to-school + seasonal hiring surge.
- **`supply_chain_automation_announcements`** — MFC, automated DCs, robotics partnerships (Ocado, Symbotic, AutoStore, Fabric, Dematic, GreyOrange, Wiliot IoT).
- **`private_label_growth`** — Aggressive private-label/own-brand growth flagged in earnings.

### Partnership & M&A

- **`ai_vendor_partnership_announcement`** — Press release naming AI startup/vendor: Afresh, Instacart AI Solutions (Cart Assistant, Caper, Storefront Pro), Daisy AI, Standard AI, Trigo, AiFi, Symphony AI, Crisp, Pendulum, Shelf Engine, Digital Wave Technology, Hivery.
- **`consulting_partnership`** — Named partnership with IBM Consulting, Accenture, Deloitte, Capgemini, Cognizant, EPAM, TCS, Infosys, Wipro on AI/digital transformation.
- **`m_and_a_tech_acquisition`** — Acquisition of technology, data, AI, or fulfillment company.
- **`innovation_lab_existence`** — Public-facing innovation lab, university research partnership, retail VC fund, accelerator participation (e.g., Kroger Innovation Lab + UC; W23 Global).
- **`pilot_program_announced`** — Press release language: "piloting," "early access," "limited rollout," "test market." *High confidence:* named tech + named stores + named timeline.

### Regulatory & Compliance

- **`fsma_204_exposure`** — Grocer carries Food Traceability List items (produce, leafy greens, seafood, deli salads, soft cheeses, nut butters) with US distribution.
- **`traceability_tech_investment`** — Partnership with ReposiTrak, Trustwell, Wiliot, IBM Food Trust, GS1, FoodLogiQ, Trakkey.
- **`snap_ebt_online_expansion`** — Announcement of SNAP/EBT online acceptance, especially via DoorDash, Instacart, or Walmart Pay.
- **`recall_event_history`** — FDA/USDA recall events involving the retailer over last 24 months.
- **`sustainability_reporting_complexity`** — ESG reports referencing emissions tracking, food-waste reduction targets, Scope 3 supplier data collection.

### Labor / Union

- **`ufcw_contract_expiration`** — UFCW or Teamsters contract expiration within next 12 months at named banners.
- **`recent_strike_activity`** — Strike, strike authorization, or work stoppage in last 18 months.
- **`wage_increase_pressure`** — Earnings-call commentary on "wage inflation," "minimum wage increases," "labor cost pressure" + state-level minimum-wage law changes.
- **`automation_contract_language`** — Public union statements opposing automation specifically (e.g., Teamsters Local 745 autonomous-truck operator requirements).

### Financial

- **`capex_growth_yoy`** — YoY change in capex with tech/digital breakdown.
- **`revenue_pressure`** — Same-store-sales decline/stagnation over 2+ quarters.
- **`debt_issuance_for_technology`** — 8-K filings, term-loan agreements, bond prospectuses citing "technology investment" or "digital transformation" as use of proceeds.
- **`funding_round_grocer_adjacent`** — Press release of seed/Series A/B raise for tech-forward private grocers / YC-backed entrants (Vori, Vendora, Kirana AI) where use-of-funds includes AI buildout.
- **`e_commerce_profitability_signal`** — Earnings language on "e-commerce profitability" or "digital margin."

### Competitive Pressure

- **`competitor_ai_announcement_in_same_region`** — Competing chain's AI announcement against target's overlapping geography (Walmart Sparky → Aldi/Dollar General/regionals; Kroger Gemini → Albertsons/Publix/H-E-B).
- **`market_share_shift`** — Numerator/Circana/Nielsen/NIQ report of share loss/gain pressure.
- **`peer_benchmarking_panic_signal`** — Analyst notes, trade press, exec interviews: "we cannot fall behind," "table stakes now," "must respond," "Walmart effect."

### Composite

- **`digital_maturity_score`** — Composite 1-5 scale across: data foundation, cloud posture, customer-data unification, AI deployments in production, organizational governance.
- **`ai_narrative_consistency`** — Consistency of AI narrative across earnings calls, press releases, careers page, exec LinkedIn vs. contradictory.
- **`vendor_pain_signal`** — Reviews/Reddit/tech press complaints about current vendors ("Genesys complexity," "NICE pricing," "Five9 outages," legacy IVR frustration).
- **`cultural_readiness`** — Glassdoor + LinkedIn employee posts on "innovation," "experimentation," "data-driven" vs "siloed," "legacy," "bureaucratic."

---

## Sub-Industry: Home & Furniture Retail (US)

**Universe:** Wayfair, Williams-Sonoma (Pottery Barn, West Elm, WS, PB Kids/Teen, Rejuvenation, Mark & Graham), IKEA, Ashley HomeStore, RH, Crate & Barrel/CB2, Living Spaces, Rooms To Go, Bob's Discount Furniture, Casper, Purple Innovation, Saatva, Article, Burrow, Floyd, Joybird, Maiden Home, Outer, CITY Furniture, ~1,000 regional independents.

### Hiring

- **`hiring_conversational_voice_ai_roles`** — Hiring VP of Customer Experience, Chief Customer Officer, or Head of CX. Weight 2.00 / Conf 3. Query: `site:linkedin.com/jobs OR site:greenhouse.io OR site:lever.co "{{company_name}}" ("VP Customer Experience" OR "Vice President Customer Experience" OR "Chief Customer Officer" OR "VP CX" OR "Head of Customer Experience" OR "Director of Customer Experience" OR "CCO")`. *Rationale:* The buyer persona being hired — fresh hire signals new budget and openness to CX tooling. ABM Engine's champion is a VP/Director of CX.
- **`hiring_ai_ml_leadership`** — Evidence of a large customer service or contact center operation (LinkedIn profiles, Glassdoor mentions, company careers page). Weight 1.80 / Conf 3. Query: `site:linkedin.com "{{company_name}}" ("customer service" OR "contact center" OR "call center" OR "customer care") OR site:glassdoor.com "{{company_name}}" ("customer service" OR "call center" OR "contact center")`. *Rationale:* Large manual CX headcount = high automation ROI. Evidence of an active CS/contact-center workforce — LinkedIn profiles in those roles or Glassdoor reviews mentioning the team — confirms the operational footprint ABM Engine targets.
- **`hiring_cx_automation_specialist`** — Hiring Head or Director of Contact Center Operations or Customer Service Operations. Weight 1.60 / Conf 3. Query: `site:linkedin.com/jobs OR site:greenhouse.io OR site:lever.co "{{company_name}}" ("Head of Contact Center" OR "Director of Contact Center" OR "VP Contact Center" OR "Director of Customer Service Operations" OR "VP Customer Service" OR "Director of Customer Care")`. *Rationale:* Contact center leadership hire signals CX infrastructure budget and a dedicated owner who evaluates tools like ABM Engine.
- **`hiring_seasonal_contact_center_surge`** — Seasonal/peak-season CX hiring surge (>50 open CX reqs). Weight 1.20 / Conf 3.
- **`hiring_recsys_personalization_engineers`** — Recommendation systems, visual search, product discovery ML. Weight 1.20 / Conf 3.
- **`hiring_supply_chain_forecasting_analytics`** — Demand forecasting, inventory analytics, supply chain ML. Weight 1.10 / Conf 3.
- **`hiring_rpa_automation_developer`** — RPA developer / automation engineer / process automation roles. Weight 1.00 / Conf 3.
- **`hiring_mlops_data_platform`** — Head of CX Technology, Customer Experience Technology Manager, or Digital Service leader exists at the company (LinkedIn profile). Weight 1.50 / Conf 3. Query: `site:linkedin.com "{{company_name}}" ("CX technology" OR "customer experience technology" OR "contact center technology" OR "digital customer service" OR "customer service technology" OR "VP Customer Experience Technology" OR "Director of CX Technology")`. *Rationale:* A dedicated CX technology owner signals active budget for contact center tooling and willingness to evaluate ABM Engine.
- **`hiring_ar_3d_computer_vision_specialist`** — AR/VR engineering, 3D modeling, CV for products. Weight 0.90 / Conf 3.
- **`hiring_head_of_ecommerce_digital`** — VP or Head of E-commerce / Chief Digital Officer exists at the company (LinkedIn profile or press coverage). Weight 1.30 / Conf 3. Query: `site:linkedin.com "{{company_name}}" ("VP E-Commerce" OR "VP Ecommerce" OR "Head of E-Commerce" OR "Chief Digital Officer" OR "VP Digital" OR "Head of Digital" OR "Director of E-Commerce" OR "Director of Digital Experience")`. *Rationale:* An identifiable digital/e-commerce leader means there is a dedicated owner of the digital customer surface where ABM Engine's AI mediation layer operates — a VP E-commerce or CDO is a secondary champion or at minimum a stakeholder in CX tooling decisions.

### Funding & Financial

- **`funding_series_b_plus_dtc_furniture`** — Series B+ raise in last 24 months. Weight 1.30 / Conf 4. Query: `site:crunchbase.com OR site:techcrunch.com OR site:pitchbook.com ("{{company_name}}") ("Series B" OR "Series C" OR "Series D" OR "growth round") furniture`.
- **`funding_pe_ownership_buyout`** — PE-backed or recent LBO/buyout. Weight 1.40 / Conf 4. *Rationale:* PE-backed firms mandate EBITDA improvement = automation budget.
- **`earnings_ai_mention_count`** — Executive public statement committing to AI, automation, or agentic strategy (trade press, press release, IR page, CEO interview). Works for private AND public companies. Weight 1.50 / Conf 4. Query: `"{{company_name}}" ("artificial intelligence" OR "AI strategy" OR "agentic" OR "automation" OR "machine learning" OR "generative AI") (site:furnituretoday.com OR site:retaildive.com OR site:modernretail.co OR site:businesswire.com OR site:prnewswire.com OR site:globenewswire.com)`. *Rationale:* Replaces earnings-transcript-only check (which misses private companies) with a broader sweep of press releases and trade press — same intent (has leadership publicly committed to AI?) but reachable by Exa for any company regardless of public/private status.
- **`earnings_margin_pressure_cost_savings_language`** — Margin pressure or cost-takeout language in latest earnings call. Weight 1.30 / Conf 3.
- **`tenk_mdna_technology_investment`** — 10-K MD&A mentions tech investment, digital transformation, or AI. Weight 1.20 / Conf 4.
- **`mna_tech_acquisition`** — Acquired AI/tech capability or was acquired by larger retailer/PE in last 24 months. Weight 1.20 / Conf 4.
- **`ipo_s1_filing_tech_disclosure`** — Recent IPO/S-1 with technology investment disclosure. Weight 1.10 / Conf 4.

### Tech Stack

- **`techstack_modern_cloud_contact_center`** — Cloud CCaaS (Five9, NICE CXone, Talkdesk, Genesys Cloud, Amazon Connect, Twilio Flex). Weight 1.50 / Conf 4. *Rationale:* Single best deterministic signal for ABM Engine voice CX agent fit.
- **`techstack_chatbot_platform_in_use`** — Ada, Intercom Fin, Forethought, Kustomer, Cresta, ASAPP, LivePerson, Drift, Gorgias AI. Weight 1.20 / Conf 4.
- **`techstack_zendesk_salesforce_service_cloud`** — Customer service platform: Zendesk, Salesforce Service Cloud, Kustomer, Freshdesk, Help Scout. Weight 1.00 / Conf 4.
- **`techstack_shopify_plus`** — Uses Shopify Plus. Weight 1.10 / Conf 5.
- **`techstack_enterprise_commerce_platform`** — Salesforce Commerce Cloud, Adobe Commerce/Magento, BigCommerce, custom. Weight 0.90 / Conf 4.
- **`techstack_ar_3d_visualization_vendor`** — 3D Cloud, Threekit, Cylindo (Chaos), Hapticmedia, Roomy for 3D/AR. Weight 1.10 / Conf 4. *Rationale:* Furniture-distinctive.
- **`techstack_recommendation_search_vendor`** — Algolia, Constructor.io, Bloomreach, Coveo, Klevu, Searchspring, Nosto. Weight 0.90 / Conf 4.
- **`techstack_supply_chain_erp`** — Manhattan Associates, Blue Yonder, o9, Coupa, NetSuite, SAP, modern WMS/ERP. Weight 1.00 / Conf 4.
- **`techstack_data_platform`** — Snowflake, Databricks, BigQuery, Segment, mParticle. Weight 1.00 / Conf 4.
- **`techstack_hyperscaler_partnership_public`** — Public case study with AWS, GCP, Azure, OpenAI, Anthropic, major LLM vendor. Weight 1.30 / Conf 5.

### CX Pain / Operational Distress

- **`cxpain_trustpilot_delivery_complaints`** — Trustpilot/BBB high volume of delivery, wait-time, CX-unresponsive complaints. Weight 1.60 / Conf 3. *Rationale:* Industry benchmark — 26% of furniture retail Trustpilot reviews mention delivery, 75% negative.
- **`cxpain_reddit_brand_complaints`** — Reddit threads (r/furniture, r/HomeImprovement, brand subs) on CX failures. Weight 1.20 / Conf 3.
- **`cxpain_app_store_reviews_chat_voice`** — iOS/Android app store reviews mention chatbot, hold time, contact frustration. Weight 1.10 / Conf 3.
- **`cxpain_glassdoor_cx_employee_signals`** — Glassdoor reviews from CX/contact center employees on understaffing/volume. Weight 1.30 / Conf 3.
- **`cxpain_bbb_accreditation_complaint_volume`** — BBB complaint volume relative to peers + accreditation status. Weight 0.90 / Conf 3.
- **`cxpain_delivery_specific_complaint_density`** — Disproportionate delivery/white-glove complaint density. Weight 1.40 / Conf 3. *Rationale:* Most furniture-specific pain signal — directly proves voice/CX agent ROI.

### Strategic Priority

- **`strategic_exec_linkedin_ai_thoughtleadership`** — CEO/CFO/CDO/CIO/CTO LinkedIn posts on AI/automation/digital transformation. Weight 1.40 / Conf 3.
- **`strategic_earnings_specific_ai_use_cases`** — Earnings call cites specific AI use cases (contact center, returns, supply chain, personalization) with metrics. Weight 1.60 / Conf 4. *Rationale:* Specificity > frequency.
- **`strategic_annual_report_tech_priority`** — 10-K/annual report lists CX tech or AI as named strategic initiative. Weight 1.30 / Conf 4.
- **`strategic_hyperscaler_partnership_announcement`** — Announced strategic partnership with AWS/GCP/Azure/Salesforce/Shopify/OpenAI/Anthropic/Perplexity. Weight 1.30 / Conf 4.
- **`strategic_innovation_lab_or_design_program`** — Innovation lab, design studio, B2B/trade program with tech pillar. Weight 0.80 / Conf 3.
- **`strategic_award_nomination_industry_press`** — Industry award nominations/wins for CX, innovation, AI (Retail Touchpoints, RIS News, NRF, RTIH AI, Furniture Today). Weight 0.70 / Conf 3.

### Volume / Scale

- **`volume_store_count_growth`** — Store count >50 OR multi-channel (DTC + physical). Weight 0.90 / Conf 4.
- **`volume_revenue_scale_threshold`** — Annual revenue >$250M. Weight 0.80 / Conf 4.
- **`volume_sku_count_catalog_complexity`** — Catalog size >100K SKUs. Weight 1.00 / Conf 3.
- **`volume_warehouse_dc_count`** — Number of DCs / fulfillment hubs. Weight 0.70 / Conf 3.
- **`volume_cx_team_size_linkedin`** — Customer service team size (LinkedIn employee filter). Weight 1.10 / Conf 3.

### Industry-Specific

- **`industry_ar_visualization_feature_live`** — Live AR "view in room" feature in mobile app or web. Weight 0.90 / Conf 4.
- **`industry_visual_search_image_shopping`** — Visual search / image-based shopping feature. Weight 0.80 / Conf 3.
- **`industry_furniture_configurator_modular`** — Product configurator for modular/customizable furniture. Weight 0.80 / Conf 3.
- **`industry_designer_trade_program`** — Designer/trade B2B program. Weight 0.70 / Conf 4.
- **`industry_white_glove_scheduling_complexity`** — White-glove delivery / assembly / inside-room delivery. Weight 1.20 / Conf 4. *Rationale:* Canonical ABM Engine voice agent use case for furniture.
- **`industry_returns_policy_complexity`** — Returns/exchange policy mentions sizing/fit/space issues. Weight 0.90 / Conf 3.
- **`industry_showroom_to_online_transition`** — Public commentary on shifting from showroom-led to digital-led. Weight 0.80 / Conf 3.

### Regulatory & External Pressure

- **`regulatory_tariff_exposure_imports`** — Material exposure to China/Vietnam/Mexico furniture tariffs (Section 232). Weight 1.30 / Conf 4.
- **`regulatory_ada_lawsuit_history`** — ADA/WCAG website accessibility lawsuit in last 24 months. Weight 0.90 / Conf 4.
- **`regulatory_ccpa_state_privacy_compliance`** — Public CCPA/state privacy compliance disclosure or breach history. Weight 0.60 / Conf 3.
- **`regulatory_supply_chain_disruption_disclosure`** — 10-K/10-Q discloses material supply chain disruption or risk. Weight 0.80 / Conf 3.

### Partnership & Ecosystem

- **`partnership_salesforce_customer_story`** — Salesforce customer story (Service Cloud, Commerce Cloud, Agentforce, Einstein). Weight 1.00 / Conf 5.
- **`partnership_shopify_plus_case_study`** — Shopify Plus customer story or partner integration. Weight 0.80 / Conf 4.
- **`partnership_speaking_at_retail_tech_conference`** — Speaker at NRF, Shoptalk, eTail, Furniture Today Leadership, Las Vegas/High Point Market tech track. Weight 0.90 / Conf 4.
- **`partnership_rila_nrf_membership`** — RILA, NRF, Home Furnishings Association (HFA) member. Weight 0.50 / Conf 3.

### Competitive / Peer Pressure

- **`competitive_direct_peer_deployed_ai`** — Direct US furniture peer publicly deployed customer-facing AI in last 12 months. Weight 1.20 / Conf 3.
- **`competitive_trade_press_ai_coverage`** — Trade press (Furniture Today, Home Accents Today, Retail Dive, Modern Retail) covering AI moves. Weight 1.00 / Conf 3.

### Digital Maturity

- **`digital_mobile_app_sophistication`** — Mobile app has AR, account management, >4.0 store rating. Weight 0.90 / Conf 4.
- **`digital_live_chat_present_on_site`** — Live chat / chatbot widget on .com homepage. Weight 0.80 / Conf 4.
- **`digital_social_commerce_active`** — Active Instagram Shop, TikTok Shop, or Pinterest commerce. Weight 0.50 / Conf 3.
- **`digital_loyalty_program_personalized`** — Loyalty program with personalization (Wayfair Rewards, WS Key Rewards). Weight 0.60 / Conf 3.
- **`digital_genai_optimization_listings`** — Catalog optimized for GEO / ChatGPT/Perplexity discoverability. Weight 1.00 / Conf 3.

### M&A / Corporate Event

- **`mna_new_ceo_cdo_cio_last_12_months`** — New CEO, CDO, CIO, CTO, or VP CX hired in last 12 months. Weight 1.50 / Conf 4. *Rationale:* Single best timing signal in B2B sales.
- **`mna_restructuring_layoff_announcement`** — Recent layoff/restructuring (CX or back office). Weight 1.10 / Conf 4. *Rationale:* CX layoffs especially indicate automation replacement.
- **`mna_bankruptcy_emergence_postchapter11`** — Emerging from Ch.11 or actively restructuring. Weight 0.80 / Conf 4.
- **`mna_office_consolidation_real_estate`** — Recent office or DC consolidation. Weight 0.60 / Conf 3.
- **`mna_executive_departure_cx_ops`** — Recent departure of senior CX/Ops leader. Weight 0.70 / Conf 3.

---

## Sub-Industry: Beauty & Personal Care (US)

**Universe:** Estée Lauder Companies (ELC), Coty, L'Oréal USA, Ulta, Sephora, e.l.f. Beauty, Bath & Body Works, Kenvue, Shiseido Americas, Hims & Hers, Crown Affair, Olaplex, indie/DTC brands.

### Hiring (20 signals)

- **`open_ai_ml_engineer_role`** — Open AI/ML Engineer req. Weight 1.5 / Conf 3. Query: `site:boards.greenhouse.io OR site:jobs.lever.co "{{company_name}}" ("Machine Learning Engineer" OR "AI Engineer" OR "Applied Scientist")`.
- **`open_conversational_voice_ai_role`** — Conversational/Voice AI role open. Weight 2.0 / Conf 4. *Rationale:* Highest-fidelity agentic intent.
- **`open_genai_llm_prompt_role`** — GenAI / LLM / Prompt engineer. Weight 1.7 / Conf 4.
- **`open_personalization_recsys_role`** — Personalization / RecSys engineer. Weight 1.4 / Conf 3. *Rationale:* Beauty's #1 AI use case (shade match, skin diagnostics).
- **`open_mlops_aiplatform_role`** — MLOps / AI Platform role (Vertex AI, Databricks Mosaic, Snowflake Cortex). Weight 1.3 / Conf 3.
- **`open_computer_vision_role`** — Computer Vision engineer. Weight 1.4 / Conf 3. *Rationale:* AR try-on / shade-match / skin-analysis programs.
- **`open_data_engineer_analytics_role`** — Data / Analytics engineer. Weight 0.8 / Conf 2.
- **`open_ai_pm_role`** — AI Product Manager. Weight 1.6 / Conf 4.
- **`open_head_of_ai_role`** — Head of AI / VP, AI / Chief AI Officer / Director, AI. Weight 2.0 / Conf 5.
- **`open_cx_contact_center_modernization_role`** — Contact Center / CX modernization role (CCaaS, Genesys, Five9, NICE, Talkdesk). Weight 1.5 / Conf 3.
- **`open_digital_transformation_lead`** — Digital Transformation Lead. Weight 0.8 / Conf 2.
- **`open_ecommerce_merchandising_ai_role`** — Ecommerce / Merchandising AI role. Weight 1.3 / Conf 3.
- **`open_marketing_ai_role`** — MarTech / Marketing AI role. Weight 0.9 / Conf 2.
- **`open_supply_chain_forecasting_ai_role`** — Supply chain / demand forecasting AI. Weight 1.3 / Conf 3.
- **`tech_hiring_volume_spike`** — Total tech hiring volume > 1.5× trailing 6-month median. Weight 0.7 / Conf 2.
- **`platform_skill_specific_posting`** — JD names specific AI platform (Salesforce Einstein, Adobe Sensei/Firefly, Dynamics Copilot, Shopify AI, Klaviyo AI, Snowflake Cortex, Databricks Mosaic, Copilot). Weight 1.6 / Conf 4.
- **`open_ba_training_ai_role`** — Beauty advisor / clienteling AI enablement role. Weight 1.2 / Conf 3.
- **`open_fraud_returns_abuse_role`** — Returns abuse / loss prevention AI role. Weight 1.1 / Conf 3.
- **`nyc_sf_la_ai_hiring_cluster`** — NYC/SF/LA AI hiring cluster (geographic concentration in beauty-tech hubs). Weight 0.7 / Conf 2.
- **`ai_role_compensation_high`** — Posted comp band ≥$200K base for AI role. Weight 1.2 / Conf 3.

### Leadership / Executive (10 signals)

- **`new_cdo_cto_cio_last_12mo`** — New CDO/CTO/CIO in last 12 months. Weight 2.0 / Conf 4.
- **`new_chief_ai_officer`** — New Chief AI Officer / Head of AI. Weight 2.0 / Conf 5. *Rationale:* Strongest single executive signal.
- **`new_vp_cx_contact_center`** — New VP Customer Experience / Contact Center. Weight 1.6 / Conf 4.
- **`new_chief_data_officer`** — New CDO. Weight 1.6 / Conf 4.
- **`new_vp_ecommerce_digital`** — New VP Ecommerce / Digital. Weight 1.5 / Conf 4.
- **`new_cmo_digital_ai_background`** — New CMO with digital/AI background. Weight 1.2 / Conf 3.
- **`new_coo_modernization_mandate`** — New COO with operations modernization mandate. Weight 1.3 / Conf 3.
- **`board_ai_tech_appointment`** — Board appointment with AI/tech background. Weight 1.0 / Conf 2.
- **`key_tech_leader_departure`** — Departure of CIO/CTO/CDO. Weight 1.2 / Conf 3.
- **`linkedin_role_change_6mo`** — LinkedIn role-change event in last 6 months (Sales Navigator alert). Weight 1.6 / Conf 4.

### Funding & Financial (12 signals)

- **`series_a_to_d_last_18mo`** — Series A–Growth round in last 18 months. Weight 1.3 / Conf 3.
- **`ipo_last_24mo`** — IPO in last 24 months. Weight 1.5 / Conf 4.
- **`pe_strategic_investment`** — PE/VC with AI portfolio takes stake (True Beauty Ventures / Prelude / Imaginary / Forerunner / L'Oréal BOLD / Unilever Ventures / Shiseido SBVC). Weight 1.0 / Conf 3.
- **`acquired_by_conglomerate`** — Acquired by ELC, L'Oréal, Unilever, Coty, P&G, Kenvue, Shiseido, Puig, e.l.f. Weight 1.6 / Conf 4.
- **`revenue_milestone_announced`** — $100M / $500M / $1B revenue milestone. Weight 0.9 / Conf 2.
- **`profitability_inflection`** — First profitable quarter / EBITDA positive. Weight 0.8 / Conf 2.
- **`layoffs_announced_warn`** — Layoffs / WARN filed in last 12 months. Weight 1.7 / Conf 4. *Rationale:* Automation substitute mandate.
- **`earnings_call_ai_mention_count`** — "AI"/"automation"/"agentic" mention count ≥5 on last earnings call. Weight 2.0 / Conf 5.
- **`tenK_ai_risk_factor_mention`** — 10-K risk factor includes AI/digital disruption. Weight 1.2 / Conf 3.
- **`eightK_tech_investment`** — 8-K filing referencing tech/AI investment. Weight 1.6 / Conf 4.
- **`crowdfunding_milestone`** — Crowdfunding (Republic, StartEngine, Wefunder) over $1M. Weight 0.5 / Conf 1.
- **`cost_savings_program_named`** — Public cost-savings program names $ target (ELC PRGP $1.5–1.7B / Coty $700M / Kenvue $350M). Weight 1.7 / Conf 4.

### Tech Stack (22 signals)

- **`stack_commercetools`** — commercetools detected. Weight 1.5 / Conf 4.
- **`stack_salesforce_commerce_cloud`** — Salesforce Commerce Cloud / Einstein detected. Weight 1.2 / Conf 3.
- **`stack_shopify_plus`** — Shopify Plus detected. Weight 1.1 / Conf 3.
- **`stack_sap_oracle_erp`** — SAP / Oracle ERP detected (e.l.f. SAP, P&G SAP). Weight 0.8 / Conf 2.
- **`stack_snowflake_or_databricks`** — Snowflake or Databricks deployment. Weight 1.4 / Conf 4.
- **`stack_segment_mparticle_treasuredata`** — CDP detected. Weight 1.2 / Conf 3.
- **`stack_klaviyo`** — Klaviyo detected. Weight 0.9 / Conf 2.
- **`stack_attentive_postscript`** — SMS marketing platform. Weight 0.8 / Conf 2.
- **`stack_bazaarvoice`** — Bazaarvoice on PDP. Weight 0.9 / Conf 2.
- **`stack_yotpo`** — Yotpo on PDP. Weight 0.9 / Conf 2.
- **`stack_okendo_powerreviews_stamped`** — Other UGC platform. Weight 0.6 / Conf 1.
- **`stack_perfect_corp_modiface_revieve_haut_banuba`** — AR try-on / skin diagnostic widget detected. Weight 2.0 / Conf 5. *Rationale:* Beauty-specific top adjacency.
- **`stack_lily_ai_bloomreach_constructor_algolia_coveo_klevu_syte`** — Personalization / search AI vendor. Weight 1.6 / Conf 4.
- **`stack_optimove`** — Optimove deployed (Sephora). Weight 1.5 / Conf 4.
- **`stack_ccaas_genesys_nice_five9_talkdesk_amazon_connect_twilio`** — CCaaS in use. Weight 1.6 / Conf 4.
- **`stack_chat_drift_intercom_gladly_kustomer_gorgias_ada_cresta`** — Chat / chatbot platform. Weight 1.5 / Conf 4.
- **`stack_voice_ai_replicant_polyai_hume_observe_pindrop_cresta_voice`** — Voice AI platform. Weight 2.0 / Conf 5.
- **`stack_loyalty_yotpo_smileio_loyaltylion_antavo_punchh_eagleeye`** — Loyalty platform identified. Weight 0.8 / Conf 2.
- **`stack_pim_dam_salsify_akeneo_bynder_widen`** — PIM/DAM detected. Weight 1.1 / Conf 3.
- **`stack_pos_aptos_newstore_manhattan_lightspeed_shopifypos`** — Unified commerce / POS. Weight 0.8 / Conf 2.
- **`stack_analytics_heap_amplitude_mixpanel_thoughtspot`** — Product analytics / semantic-layer BI. Weight 0.9 / Conf 2.
- **`stack_hyperscaler_publicly_named`** — Hyperscaler partnership publicly named (AWS / GCP / Azure / OCI). Weight 1.2 / Conf 3.

### Strategic / Earnings (10 signals)

- **`transcript_ai_mentions_gte_5`** — ≥5 mentions of "AI"/"artificial intelligence" on most recent earnings call. Weight 1.6 / Conf 4.
- **`transcript_generative_ai_mention`** — ≥1 mention of "generative AI" or "GenAI". Weight 1.6 / Conf 4.
- **`transcript_agentic_mention`** — ≥1 mention of "agentic" / "AI agent" / "voice agent". Weight 2.0 / Conf 5. *Rationale:* Strongest leading indicator.
- **`transcript_automation_mention`** — ≥2 mentions of "automation"/"automate". Weight 1.1 / Conf 3.
- **`transcript_personalization_mention`** — ≥2 mentions of "personalization". Weight 0.9 / Conf 2.
- **`transcript_demand_forecasting_ai`** — "demand forecasting"/"demand planning" with AI/ML in same paragraph. Weight 1.5 / Conf 4.
- **`investor_day_announced`** — Investor Day scheduled/held in last 6 mo. Weight 1.2 / Conf 3.
- **`named_strategic_initiative`** — Strategic initiative named ("Beauty Reimagined", "Vision 2030", "Profit Recovery and Growth Plan"). Weight 1.6 / Conf 4.
- **`capex_increase_yoy`** — YoY capex increase ≥15% per 10-K. Weight 1.2 / Conf 3.
- **`ir_press_ai_digital`** — IR press release tagged AI/digital in last 90 days. Weight 1.2 / Conf 3.

### M&A / Partnerships (8 signals)

- **`acquired_ai_or_tech_startup`** — Acquired AI/tech startup in last 24 mo (Ulta + QM Scientific; L'Oréal + ModiFace). Weight 1.9 / Conf 5.
- **`hyperscaler_partnership`** — Partnership with AWS / Google Cloud / Azure / Oracle Cloud announced. Weight 1.5 / Conf 4.
- **`ai_consortium_membership`** — Joined MACH Alliance / NRF AI Council / Beauty Tech consortium. Weight 0.9 / Conf 2.
- **`consultancy_ai_engagement`** — Engagement with Accenture, Deloitte Digital, Publicis Sapient, EY, McKinsey QuantumBlack on AI. Weight 1.5 / Conf 4.
- **`si_engagement`** — SI engagement (Tata Elxsi, Wipro, Infosys, Cognizant, Capgemini, LTIMindtree, EPAM). Weight 1.1 / Conf 3.
- **`joint_case_study_ai_vendor`** — Joint case study with named AI vendor (Salesforce, Adobe, Bloomreach, Lily AI, Persado, Yotpo, Bazaarvoice, Perfect Corp, Revieve, Ada, Cresta, Replicant, PolyAI). Weight 1.6 / Conf 4.
- **`chatgpt_or_openai_partnership`** — OpenAI / ChatGPT app or partnership announced. Weight 2.0 / Conf 5.
- **`acquired_in_last_18mo_integration_window`** — Company itself was acquired in the last 18 months. Weight 1.6 / Conf 4.

### Regulatory / Compliance (10 signals — beauty-specific)

- **`mocra_facility_registration`** — Active MoCRA cosmetic facility registration (FEI). Weight 0.7 / Conf 2.
- **`mocra_new_or_renewal_filed`** — New or biennial-renewal MoCRA filing in last 6 mo. Weight 1.0 / Conf 3.
- **`fda_warning_letter_24mo`** — FDA warning letter to company/contract manufacturer in last 24 months. Weight 1.4 / Conf 4.
- **`fda_recall_24mo`** — FDA recall (Class I/II/III) in last 24 months. Weight 1.6 / Conf 4.
- **`fda_adverse_event_dashboard_entry`** — Entry on FDA real-time cosmetic adverse-event dashboard. Weight 1.2 / Conf 3.
- **`ftc_action_or_class_action`** — FTC action or class-action greenwashing / deceptive marketing in last 24 mo. Weight 1.1 / Conf 3.
- **`state_ingredient_regulation_exposure`** — CA Prop 65 / NY ingredient ban / WA CHCC / NJ filing exposure. Weight 1.1 / Conf 3.
- **`pfas_disclosure_exposure`** — Named in FDA PFAS-in-cosmetics report (Dec 2025). Weight 1.5 / Conf 4.
- **`sec_cyber_incident_8K`** — Cyber incident disclosed via 8-K. Weight 1.6 / Conf 4.
- **`talc_asbestos_proposed_rule_exposure`** — Talc-containing product portfolio (Dec 2024 FDA proposed rule). Weight 1.1 / Conf 3.

### Volume / Operational (8 signals)

- **`store_count_growth`** — Store count change YoY ≥+5%. Weight 0.8 / Conf 2.
- **`store_count_shrinkage`** — Store count change YoY ≤−5%. Weight 1.0 / Conf 3. *Rationale:* Automation lever.
- **`new_dc_or_3pl`** — New DC or 3PL announced. Weight 1.1 / Conf 3.
- **`app_store_rank_top_50_shopping_beauty`** — App store rank in top-50 Shopping/Lifestyle in last 30 days. Weight 0.9 / Conf 2.
- **`web_traffic_spike_or_decline_25pct`** — SimilarWeb monthly traffic Δ ≥±25% YoY. Weight 0.8 / Conf 2.
- **`social_milestone`** — 1M/5M/10M follower milestone. Weight 0.5 / Conf 1.
- **`csr_ba_hiring_volume_spike`** — CSR / BA seasonal hiring spike. Weight 1.1 / Conf 3.
- **`subscription_growth_metric_disclosed`** — Subscription revenue growth disclosed in 10-Q/earnings. Weight 0.9 / Conf 2.

### Product / Launch (9 signals)

- **`launched_ai_mobile_app_or_feature`** — Launched mobile app with named AI feature in last 12 mo. Weight 1.6 / Conf 4.
- **`launched_ar_try_on`** — Launched AR try-on (Perfect Corp / ModiFace / Banuba / proprietary). Weight 1.6 / Conf 4.
- **`launched_skin_or_hair_diagnostic`** — Launched AI skin or hair diagnostic. Weight 1.6 / Conf 4.
- **`launched_personalized_product`** — Function-of-Beauty-style personalized product launch. Weight 1.3 / Conf 3.
- **`loyalty_program_v2_launched`** — New/refreshed loyalty program v2. Weight 1.2 / Conf 3.
- **`b2b_portal_launched`** — B2B portal launched (pro/salon-side). Weight 0.9 / Conf 2.
- **`wholesale_or_white_label_launched`** — New wholesale / private label channel. Weight 0.8 / Conf 2.
- **`new_region_or_country_launch`** — Launched in new region. Weight 0.8 / Conf 2.
- **`chatgpt_or_llm_storefront_launched`** — Storefront launched inside ChatGPT / LLM (Sephora Oct 2025). Weight 2.0 / Conf 5.

### Marketing / Advertising (6 signals)

- **`new_aor_hired_12mo`** — New Agency of Record hired in last 12 mo. Weight 0.9 / Conf 2.
- **`new_brand_campaign_launched`** — New brand campaign launched. Weight 0.5 / Conf 1.
- **`tiktok_shop_integration`** — TikTok Shop integration confirmed. Weight 1.2 / Conf 3.
- **`genai_advertising_case_study`** — Named in GenAI-advertising case study (AdAge/Adweek/Marketing Brew). Weight 1.6 / Conf 4.
- **`influencer_affiliate_program_launch`** — Influencer / affiliate program launched. Weight 0.5 / Conf 1.
- **`ugc_platform_deployed`** — UGC platform (Bazaarvoice / Yotpo / Pixlee / Okendo) deployed. Weight 0.9 / Conf 2.

### Awards / Recognition (6 signals)

- **`nrf_big_show_speaker`** — Speaker at NRF Big Show 2025/2026. Weight 1.1 / Conf 3.
- **`shoptalk_speaker`** — Speaker at Shoptalk / Shoptalk Fall. Weight 1.1 / Conf 3.
- **`ces_speaker_beauty_tech`** — CES speaker (beauty tech track). Weight 1.1 / Conf 3.
- **`glossy50_modernretail50_listing`** — Glossy 50 / Modern Retail 50 listing. Weight 0.9 / Conf 2.
- **`beautymatter_award`** — BeautyMatter Future50 / NEXT recognition. Weight 0.9 / Conf 2.
- **`cosmoprof_exhibitor_or_award`** — Cosmoprof North America exhibitor / award winner. Weight 0.8 / Conf 2.

### Real Estate / Footprint (4 signals)

- **`new_flagship_with_experiential_tech`** — New flagship store with magic mirrors / AR kiosks. Weight 1.1 / Conf 3.
- **`pop_up_activations_24mo`** — Pop-up activations in last 24 months. Weight 0.6 / Conf 1.
- **`hq_relocation`** — HQ relocation (Kenvue → Summit NJ). Weight 1.1 / Conf 3.
- **`innovation_center_opened`** — New innovation center / R&D lab opening. Weight 1.2 / Conf 3.

### Patent / IP (4 signals)

- **`uspto_ai_ml_patent_filing`** — USPTO patent application referencing AI/ML/CV/AR in last 24 mo. Weight 1.5 / Conf 4.
- **`uspto_trademark_ai_product_name`** — New trademark with AI-related product name. Weight 1.0 / Conf 3.
- **`published_pct_application_ar_tryon`** — PCT publication on AR try-on / virtual makeup. Weight 1.1 / Conf 3.
- **`acquired_patent_portfolio_via_ma`** — Acquired patents via M&A (L'Oréal/ModiFace pattern). Weight 1.1 / Conf 3.

### Layoffs / Restructuring (5 signals)

- **`warn_act_notice_12mo`** — WARN Act filing in last 12 months (NJ DOL, CA EDD, NY DOL, IL DCEO, MA EOLWD, OH DJFS). Weight 1.6 / Conf 4.
- **`headcount_reduction_announced`** — Public headcount reduction announcement. Weight 1.6 / Conf 4.
- **`department_consolidation`** — Department restructuring (CX/ops/digital consolidation). Weight 1.5 / Conf 4.
- **`outsourcing_announcement`** — "Outsourcing select services" language in restructuring filing (ELC PRGP). Weight 1.7 / Conf 4.
- **`back_office_function_offshoring`** — Back-office offshoring announcement. Weight 1.1 / Conf 3.

### Content / Thought Leadership (5 signals)

- **`exec_byline_beautymatter_glossy_wwd_ai`** — Executive byline / quote referencing AI/personalization/automation in BeautyMatter / Glossy / WWD / Modern Retail / Retail Dive / Cosmetics Business / Beauty Independent in last 12 mo. Weight 1.2 / Conf 3.
- **`podcast_appearance_ai`** — Podcast appearance referencing AI (Glossy Beauty, BeautyMatter, BoF Podcast, CXM Today). Weight 0.9 / Conf 2.
- **`conference_speaking_slot_ai_track`** — Conference speaking slot on AI/personalization track. Weight 1.4 / Conf 4.
- **`case_study_published_by_vendor`** — Featured as case study by Tier-1 AI vendor in last 18 mo. Weight 1.6 / Conf 4.
- **`executive_linkedin_post_ai_use_case`** — Executive's LinkedIn post referencing deployed AI use case at the company. Weight 1.1 / Conf 3.

---

## Sub-Industry: Apparel & Fashion (US)

**Universe:** Levi's, Tapestry, Nike, Lululemon, Ralph Lauren, Macy's, Stitch Fix, Walmart, Target, Gap, Old Navy, Abercrombie, Allbirds, Peloton, Rothy's, Sweaty Betty, Adidas, JD Sports, H&M, Crocs, Bloomingdale's, Apparel Group, Nordstrom, Princess Polly, LVMH brands, Kering brands, Inditex.

### Hiring & Talent

- **`open_ml_ai_roles_count`** — Open AI/ML/Data Science Job Postings (≥5 sustained). Weight 4 / Conf 3. Query: `site:greenhouse.io OR site:lever.co OR site:myworkdayjobs.com {{company_name}} ("machine learning" OR "data scientist" OR "AI engineer" OR "applied scientist" OR "MLOps")`.
- **`senior_ai_leadership_hire_18mo`** — Chief AI / Digital / Tech / Data / Transformation Officer hired in last 18 months. Weight 5 / Conf 2. *Rationale:* Highest-yield single signal.
- **`ml_platform_team_signal`** — Job postings referencing internal ML platform / feature store / MLOps. Weight 4 / Conf 2.
- **`computer_vision_roles`** — Computer Vision / Image ML hiring. Weight 4 / Conf 2.
- **`generative_ai_specific_roles`** — Generative AI / LLM / Prompt engineering roles. Weight 4 / Conf 2.
- **`data_engineering_hiring_ratio`** — Open Data Engineer / Analytics Engineer / Data Platform Engineer roles (~2:1 to data scientists). Weight 3 / Conf 2.

### Executive & Strategic Intent

- **`earnings_call_ai_mentions`** — Regex count of AI/ML/generative AI/agentic/personalization/demand forecasting in last 4 transcripts. Weight 4 / Conf 3.
- **`10k_ai_strategic_pillar`** — AI cited as strategic pillar in 10-K MD&A. Weight 4 / Conf 2.
- **`investor_day_ai_capex`** — Investor day / capital markets day with multi-year capex tied to AI. Weight 4 / Conf 2.
- **`ceo_cdo_linkedin_ai_thought_leadership`** — CEO/CFO/CDO/CTO LinkedIn posts, podcast interviews, trade-press op-eds on AI strategy. Weight 3 / Conf 2.
- **`ai_ethics_governance_statement`** — Published responsible-AI principles / AI governance framework / EU AI Act compliance language. Weight 2 / Conf 1.
- **`press_release_ai_initiative`** — First-party PR announcing AI deployment/partnership/product. Weight 4 / Conf 1.

### Technology Stack & Vendor Partnerships

- **`search_discovery_ai_vendor`** — Algolia / Bloomreach / Constructor.io / Coveo / Searchspring / Klevu / Lucidworks / Vertex AI Search detected. Weight 4 / Conf 1.
- **`data_platform_databricks_snowflake`** — Modern Data Platform deployment. Weight 4 / Conf 1.
- **`hyperscaler_ai_partnership`** — Azure OpenAI / AWS Bedrock / Vertex AI / Anthropic Claude named partnership. Weight 5 / Conf 1.
- **`personalization_recommendation_vendor`** — Dynamic Yield / Bloomreach Engagement / Salesforce Einstein / Adobe Sensei/Target / Klaviyo AI / Movable Ink / Persado / Insider / Emarsys. Weight 3 / Conf 1.
- **`virtual_tryon_fit_vendor`** — True Fit / Fit Analytics / 3DLOOK YourFit / Vue.ai Virtual Dressing Room / Veesual / FASHN / Lalaland.ai / Doji. Weight 4 / Conf 1.
- **`supply_chain_planning_vendor`** — o9 Solutions / Blue Yonder / RELEX / Kinaxis / Lokad / ToolsGroup / Centric Software AI customer. Weight 4 / Conf 1.
- **`trend_forecasting_ai_vendor`** — Heuritech / Trendalytics / Stylumia / WGSN AI / T-Fashion deployed. Weight 3 / Conf 1.
- **`product_attribution_ai_vendor`** — Lily AI / Syte / Vue.ai catalog tagging. Weight 3 / Conf 1.
- **`returns_ai_vendor`** — Optoro / Loop Returns / Narvar / ReturnGo / Newmine / Happy Returns / AfterShip Returns. Weight 3 / Conf 1.
- **`headless_composable_commerce`** — Headless/Composable (Next.js, Hydrogen, PWA Kit, Shopify Plus, SFCC, commercetools, Adobe Commerce). Weight 3 / Conf 1.
- **`cdp_deployment`** — Segment / mParticle / Tealium / Salesforce Data Cloud / Bloomreach Engagement / Treasure Data. Weight 3 / Conf 1.
- **`ai_chatbot_live_on_site`** — AI chatbot on .com or app (Drift, Intercom Fin, Ada, Sierra, Forethought, Klaviyo Customer Agent, custom Azure/OpenAI). Weight 4 / Conf 1.
- **`real_time_streaming_signals`** — Kafka / Confluent / Kinesis / Flink in JD or case studies. Weight 2 / Conf 1.
- **`vector_database_signals`** — Pinecone / Weaviate / pgvector / Qdrant / LanceDB in JDs or eng blogs. Weight 3 / Conf 1.

### CX (Probabilistic in source — reclassified)

- **`loyalty_program_ai_signals`** — Mentions in 10-K/earnings of AI-driven loyalty personalization, next-best-action, customer-LTV modeling. Weight 2 / Conf 2.
- **`cx_pain_reddit_trustpilot`** — Trustpilot, BBB, Reddit (r/[brand]), app store reviews for support waits, fit issues, return delays, irrelevant recommendations, slow checkout. Weight 2 / Conf 2.

### Funding & M&A

- **`funding_round_18mo_series_a_plus`** — Series A+ or growth-equity round / debt facility in trailing 18 months. Weight 3 / Conf 1.
- **`ai_startup_acquisition`** — Acquired AI/ML startup or acqui-hire. Weight 5 / Conf 1.
- **`ai_vc_arm_or_strategic_investment`** — Company or CVC arm made strategic investment in AI startup. Weight 3 / Conf 1.

### Live Deployments & Use Cases

- **`visual_search_live`** — Image-upload visual search functional on .com or app. Weight 4 / Conf 1.
- **`demand_forecasting_ai_disclosed`** — Public disclosure of AI-driven demand forecasting / allocation / replenishment in production. Weight 4 / Conf 2.
- **`dynamic_pricing_ai_signals`** — Disclosed AI for dynamic pricing / price elasticity / markdown optimization (Centric, invent.ai, Competera, Revionics, Hypersonix, Profitmind, Metyis). Weight 3 / Conf 2.
- **`creative_ai_marketing_disclosed`** — Generative AI for product imagery / model avatars / marketing copy / campaign creative (Parallel Pictures, Maison Meta, Lalaland, FASHN, Caimera, Raspberry AI). Weight 3 / Conf 1.
- **`design_ai_disclosed`** — AI integrated into design/PD workflow (Raspberry AI, AI.Fashion, BLNG, Style3D AI). Weight 3 / Conf 1.
- **`store_associate_ai_clienteling`** — In-store AI tools for sales associates (Microsoft/Avanade Clienteling Copilot, Kering Luce, Nordstrom Style Board). Weight 3 / Conf 1.
- **`fraud_detection_ai`** — AI-driven fraud on returns or payments (Appriss Retail, Forter, Riskified, Signifyd). Weight 2 / Conf 1.
- **`internal_genai_assistant_employee`** — Internal LLM-powered assistant for merchants / designers / planners / back-office (Walmart Wally, Levi's process-mining). Weight 3 / Conf 1.

### Volume, Scale & Pain

- **`store_count_volume`** — >100 stores OR >$500M e-commerce GMV OR >50K SKUs. Weight 3 / Conf 1.
- **`contact_center_fte_size`** — Estimated CX FTE count >200 from LinkedIn filters. Weight 2 / Conf 1.
- **`returns_volume_indicator`** — BBB/Trustpilot complaints on fit/size; 10-K returns provision growth; app reviews on sizing. Weight 3 / Conf 2.
- **`sku_count_complexity`** — >10,000 SKUs or >5 categories with size/color variants. Weight 2 / Conf 1.

### Patents, Conferences, RFPs

- **`patents_ai_ml_filed`** — USPTO/Google Patents for company as assignee on AI/ML/CV/recsys filings. Weight 3 / Conf 1.
- **`conference_speaking_slots`** — Executive speakers at NRF Big Show, Shoptalk, BoF Professional Summit, Glossy AI, AWS re:Invent retail, Databricks Data + AI Summit, Microsoft Envision. Weight 3 / Conf 1.
- **`public_rfp_ai_vendor`** — RFP on procurement portal, SEC filings, or government contracting portals for AI/ML/data science capability. Weight 4 / Conf 1.
- **`industry_award_ai_innovation`** — RTIH AI in Retail Awards, NRF Innovator Showcase, Fast Company Best Workplaces for Innovators, SJ50, BoF 500 Tech list. Weight 2 / Conf 1.

### Marketing & Media AI

- **`ai_marketing_attribution_tools`** — Northbeam / Triple Whale / Rockerbox / Measured / in-house MMM. Weight 2 / Conf 1.
- **`social_commerce_ai_tiktok`** — Active TikTok Shop / Instagram Shopping with AI creative tools / Pinterest API. Weight 2 / Conf 1.
- **`agentic_commerce_chatgpt_perplexity`** — Brand integrated for purchase/checkout via ChatGPT, Perplexity, Walmart Sparky, Amazon Rufus, Google Vertex AI shopping. Weight 4 / Conf 1.

---

## Sub-Industry: Consumer Electronics (US Mid-Market)

**Universe ($150M–$5B revenue):** Sonos, GoPro, Vizio, Roku, Logitech, Turtle Beach, Skullcandy, iRobot, Anker, Peloton, Whoop, Oura, SharkNinja, Nautilus, Garmin, Masimo, Universal Electronics, Plantronics/Poly (HP), Harman, JLab, Master & Dynamic, Eight Sleep, Hydrow, B&H Photo, Adorama, Micro Center, Crutchfield.

### Hiring (Greenhouse, Lever, LinkedIn Jobs, Ashby, Workday)

- **`hiring_conversational_ai_role`** — Active Conversational AI / Voice AI role. Conf 0.9 / Weight 1.0. Query: `site:boards.greenhouse.io OR site:jobs.lever.co "{company}" ("Conversational AI" OR "Voice AI" OR "Voice Agent")`.
- **`hiring_contact_center_ai`** — Contact Center / CCaaS AI role. Conf 0.9 / Weight 0.9.
- **`hiring_head_of_ai`** — Head of AI / Chief AI Officer hire. Conf 0.85 / Weight 0.9.
- **`hiring_ml_agent_engineer`** — ML/AI Engineer with agent/LLM skills (LangChain, LangGraph, OpenAI Agents SDK, Anthropic, agentic). Conf 0.85 / Weight 0.8.
- **`hiring_cx_director_recent`** — Recent senior CX / customer-care leadership hire. Conf 0.7 / Weight 0.7.
- **`hiring_volume_cx_agents`** — Mass CX / contact-center agent hiring (>10 active reqs). Conf 0.75 / Weight 0.6.
- **`hiring_returns_warranty_ops`** — Returns / RMA / warranty ops manager hire. Conf 0.8 / Weight 0.7.
- **`hiring_jd_named_vendor`** — JD names specific CX-AI vendor (Genesys Cloud, Five9, NICE CXone, Talkdesk, Amazon Connect, Cresta, Sierra, PolyAI, Decagon, Ada, Forethought). Conf 0.95 / Weight 0.95.
- **`hiring_voice_ai_engineer`** — Voice/Speech ML engineer (ASR/TTS/voice AI/speech model). Conf 0.85 / Weight 0.85.
- **`hiring_automation_engineer_cx`** — Automation/RPA engineer in CX function. Conf 0.75 / Weight 0.7.

### Tech Stack (BuiltWith, Wappalyzer, Apollo intent, public docs)

- **`tech_ccaas_genesys`** — Uses Genesys Cloud CX. Conf 0.9 / Weight 0.9.
- **`tech_ccaas_five9_nice_talkdesk`** — Uses Five9 / NICE CXone / Talkdesk / 8x8 Contact Center. Conf 0.9 / Weight 0.9.
- **`tech_amazon_connect`** — Amazon Connect + Lex. Conf 0.85 / Weight 0.8.
- **`tech_salesforce_service_cloud`** — Salesforce Service Cloud + Einstein. Conf 0.9 / Weight 0.85.
- **`tech_zendesk`** — Zendesk + Zendesk AI. Conf 0.85 / Weight 0.7.
- **`tech_gladly_kustomer`** — Modern CX desk (Gladly / Kustomer). Conf 0.85 / Weight 0.8.
- **`tech_ecommerce_shopify_plus`** — Runs on Shopify Plus. Conf 0.95 / Weight 0.5.
- **`tech_returns_loop_aftership_narvar`** — Returns platform (Loop / AfterShip / Narvar / Happy Returns). Conf 0.95 / Weight 0.6.
- **`tech_data_platform_snowflake_databricks`** — Snowflake / Databricks / Segment / mParticle. Conf 0.7 / Weight 0.5.
- **`tech_legacy_ivr`** — Legacy on-prem IVR / PureConnect / Avaya / Cisco UCCE / Genesys Engage. Conf 0.8 / Weight 0.9. *Rationale:* Forced-migration target (Genesys sunsetting PureConnect).
- **`tech_ai_vendor_case_study`** — Listed as customer on AI vendor case-study page (sierra.ai, poly.ai, replicant.com, decagon.ai, ada.cx, forethought.ai, cresta.com). Conf 0.95 / Weight 0.95.
- **`tech_crm_hubspot_or_sf_d2c`** — Modern CRM (Salesforce / HubSpot). Conf 0.85 / Weight 0.4.

### Executive

- **`exec_ai_post_linkedin`** — C-suite/VP LinkedIn posts on AI/automation/agentic CX. Conf 0.65 / Weight 0.7.
- **`exec_recent_caio_hire`** — CAIO / Chief Digital Officer hired in last 12 months. Conf 0.85 / Weight 0.85.
- **`exec_cco_cxo_departure`** — Chief Customer Officer / VP CX departure. Conf 0.65 / Weight 0.6.
- **`exec_speaker_cx_conf`** — Speaker at CCW, NRF, Shoptalk, Enterprise Connect, AI4. Conf 0.9 / Weight 0.8.
- **`exec_podcast_appearance_cx`** — Exec podcast appearance on CX/AI shows. Conf 0.65 / Weight 0.5.
- **`exec_genai_initiative_announced`** — Company-wide GenAI initiative announced. Conf 0.9 / Weight 0.9.

### Business Pain / Scale

- **`pain_high_return_rate_disclosed`** — Disclosed return rate >12% in 10-K, investor deck, or news. Conf 0.85 / Weight 0.85.
- **`pain_trustpilot_low_score`** — Trustpilot ≤3.0 with high "customer service" complaint volume. Conf 0.85 / Weight 0.7.
- **`pain_bbb_complaint_volume`** — BBB complaints >500 in last 3 years. Conf 0.85 / Weight 0.6.
- **`pain_reddit_subreddit_complaints`** — Active brand subreddit with weekly "support" complaints. Conf 0.7 / Weight 0.6.
- **`pain_app_store_review_cx`** — App store reviews citing "support" in 1-star reviews. Conf 0.85 / Weight 0.6.
- **`pain_seasonal_volume_strain`** — Hires 100+ seasonal CX agents annually. Conf 0.85 / Weight 0.7.
- **`pain_warranty_program_active`** — Extended-warranty / care plan publicly offered. Conf 0.9 / Weight 0.6.
- **`pain_recent_cx_layoffs`** — Public reduction in CX/support headcount. Conf 0.9 / Weight 0.85.
- **`pain_outsourced_bpo_signal`** — Currently uses BPO (Concentrix, Teleperformance, GlowTouch, Fusion CX, Sutherland). Conf 0.7 / Weight 0.8.
- **`pain_cpsc_recall_event`** — CPSC recall in last 24 months. Conf 0.95 / Weight 0.75.
- **`pain_high_call_volume_disclosed`** — Annual call volume disclosed in earnings (>500K = enterprise voice opportunity). Conf 0.85 / Weight 0.85.

### Strategic (10-K, earnings transcripts, investor decks)

- **`strat_10k_ai_mention`** — "Artificial intelligence" mentioned 3+ times in latest 10-K. Conf 0.85 / Weight 0.8.
- **`strat_earnings_cost_reduction_language`** — "Operational efficiency / cost reduction" phrasing in last 4 earnings calls. Conf 0.7 / Weight 0.7.
- **`strat_genai_capex_announced`** — Announced GenAI capex / partnership in earnings. Conf 0.95 / Weight 0.9.
- **`strat_dtc_expansion`** — D2C/D2C share of revenue growing in disclosures. Conf 0.85 / Weight 0.7.
- **`strat_subscription_services_revenue`** — Subscription/services revenue line item disclosed. Conf 0.9 / Weight 0.75.
- **`strat_international_expansion`** — Multi-language/international expansion stated. Conf 0.85 / Weight 0.6.
- **`strat_activist_investor`** — Activist investor / proxy fight (Sonos 2024, Roku). Conf 0.9 / Weight 0.8.
- **`strat_vendor_named_in_investor_deck`** — CCaaS/CX-AI vendor named in investor deck or annual report. Conf 0.95 / Weight 0.95.

### Funding / Financial Health

- **`fund_recent_series_c_plus`** — Recent Series C+ / growth round ($50M+). Conf 0.9 / Weight 0.7.
- **`fund_pe_owned`** — PE-owned (currently or recent acquisition). Conf 0.9 / Weight 0.85.
- **`fund_ipo_or_spac`** — Recent IPO / SPAC / S-1 filing. Conf 0.9 / Weight 0.7.
- **`fund_ai_capability_acquisition`** — Acquired AI/CX tech company. Conf 0.95 / Weight 0.85.
- **`fund_profitability_pressure`** — Net loss disclosed and stable/widening. Conf 0.7 / Weight 0.6.

### Product / Category

- **`prod_companion_app`** — Has companion mobile app. Conf 0.95 / Weight 0.5.
- **`prod_smart_connected`** — Wi-Fi/BT connected product (setup support load). Conf 0.9 / Weight 0.6.
- **`prod_subscription_bundle`** — Hardware-plus-subscription model. Conf 0.95 / Weight 0.7.
- **`prod_own_ai_features`** — Has shipped AI features in own products. Conf 0.85 / Weight 0.6.
- **`prod_recent_major_launch`** — Major new product launched in last 6 months. Conf 0.85 / Weight 0.5.
- **`prod_recall_or_quality_issue`** — Active recall or known quality issue. Conf 0.95 / Weight 0.8.

### Partnership / Ecosystem

- **`partner_named_ai_vendor_partnership`** — Public partnership with AI/CX vendor. Conf 0.95 / Weight 0.9.
- **`partner_conference_sponsorship`** — Sponsor of AI/CX conference (CCW, Enterprise Connect, AI4). Conf 0.85 / Weight 0.6.
- **`partner_cx_consortium_member`** — Member of CXPA, ICMI advisory board. Conf 0.65 / Weight 0.4.

### Regulatory / Compliance

- **`reg_ftc_enforcement`** — FTC enforcement / consent decree in last 36 months. Conf 0.9 / Weight 0.7.
- **`reg_ccpa_state_privacy_role`** — Privacy/compliance hire (DPO, Privacy Counsel). Conf 0.8 / Weight 0.4.
- **`reg_right_to_repair`** — Subject to right-to-repair legislation pressure. Conf 0.6 / Weight 0.4.

### Competitive / Market

- **`comp_competitor_deployed_agentic_ai`** — Direct competitor publicly deployed agentic AI. Conf 0.85 / Weight 0.8.
- **`comp_market_share_loss`** — Disclosed market share loss YoY. Conf 0.8 / Weight 0.6.
- **`comp_dtc_marketplace_shift`** — Shift away from marketplaces to DTC mix. Conf 0.85 / Weight 0.55.

---

# INDUSTRY: FINANCIAL SERVICES

---

## Sub-Industry: Auto Loans & Auto Financing (US)

**Universe:** Ally Financial, Capital One Auto Finance, GM Financial, Toyota Financial Services, Chase Auto, Credit Acceptance, Westlake Financial, Carvana, Lendbuzz, Upstart, Pagaya, Ford Motor Credit, Wells Fargo Auto, Bank of America Auto, Santander Consumer USA, Stellantis Financial Services, Hyundai Capital America, Nissan Motor Acceptance, Mercedes-Benz Financial, Honda Financial, Navy Federal, Consumer Portfolio Services, plus mid-market banks, credit unions, captives, BHPH/subprime specialists, refi marketplaces.

### Hiring

- **`open_ai_ml_engineer_roles`** — Open ML/AI engineering roles. Strength: High. Query: `site:linkedin.com/jobs "{{company_name}}" ("machine learning engineer" OR "ML engineer" OR "AI engineer")`.
- **`open_data_scientist_roles`** — Open data scientist roles. Strength: High. Query: `site:linkedin.com/jobs "{{company_name}}" "data scientist"`.
- **`open_mlops_platform_roles`** — MLOps / ML platform / ML infrastructure roles. Strength: High.
- **`open_conversational_voice_ai_roles`** — Conversational AI / Voice AI / NLP engineer / speech roles. Strength: Very High. Direct match to ABM Engine ICP.
- **`open_llm_prompt_engineer_roles`** — LLM / Prompt engineer / generative AI roles. Strength: Very High.
- **`open_data_engineering_roles`** — Data engineer / analytics engineer roles. Strength: Medium.
- **`open_responsible_ai_roles`** — Responsible AI / AI governance / model risk roles. Strength: High.
- **`open_rpa_automation_engineer_roles`** — RPA / UiPath / Blue Prism / automation engineer roles. Strength: Medium.
- **`ai_product_manager_role`** — AI Product Manager. Strength: High.
- **`ai_hiring_velocity_trend`** — Count of AI roles posted in last 90 days vs prior 90 — momentum metric. Strength: Very High.
- **`team_size_data_science_linkedin`** — Headcount of data/AI staff via LinkedIn People search. Strength: Medium.
- **`india_offshore_ai_hub_signal`** — Auto captives building Bangalore/Hyderabad AI hubs. Strength: Medium.

### Leadership & Executive

- **`chief_ai_officer_appointed`** — CAIO appointment within 24 months. Strength: Very High. *Rationale:* Strongest signal of board-level AI commitment.
- **`chief_data_officer_present`** — CDO/CDAO presence. Strength: High.
- **`chief_digital_officer_present`** — Chief Digital Officer / CDIO present. Strength: Medium.
- **`new_cio_cto_last_24_months`** — Tech leadership refresh in last 24 months. Strength: High.
- **`exec_speaker_at_ai_event`** — Speaker at Money 20/20, AFS, AFSA VFC, Databricks Summit, VB Transform. Strength: High.
- **`linkedin_thought_leadership_ai`** — Exec posting frequency about AI/automation. Strength: Medium.
- **`board_member_with_ai_background`** — Board member with GenAI/LLM deployment expertise. Strength: Medium.
- **`legacy_tech_exec_departure`** — CIO turnover signaling pending transformation. Strength: Low-Medium.
- **`ceo_letter_ai_mentions`** — CEO shareholder letters in annual reports / 10-K. Strength: High.
- **`executive_of_year_award_innovation`** — AFN Executive of the Year often spotlights tech leaders. Strength: Medium.

### Funding & Financial

- **`recent_funding_round_18mo`** — Fresh capital often funds tech transformation. Strength: High.
- **`ipo_or_spac_event`** — Public-market scrutiny accelerates AI disclosure. Strength: High.
- **`ma_acquired_ai_company`** — Buying AI capability is strongest M&A signal. Strength: Very High.
- **`strategic_investment_from_ai_vc`** — a16z, Sequoia, Insight, Bain Capital Ventures backing. Strength: Medium.
- **`ai_mentions_in_10K`** — Count of AI / ML / generative AI / automation in latest 10-K vs prior year. Strength: Very High.
- **`ai_mentions_earnings_transcript_trend`** — Quarterly mention count rising. Strength: Very High.
- **`ai_as_risk_factor_10K`** — Adding AI as 10-K risk factor (CACC 2025) signals materiality. Strength: Medium.
- **`tech_capex_disclosure`** — Public $ figure for tech/AI investment (BofA $3B). Strength: Medium.
- **`cost_cutting_automation_announce`** — "Efficiency program" + "automation" in earnings. Strength: High.
- **`securitization_volume_growth`** — High ABS issuance = scale where AI ROI is largest. Strength: Low.
- **`stock_underperformance_pressure`** — Stocks trading at deep discounts (<70% book). Strength: Medium.

### Technology Stack & Vendor

- **`databricks_customer`** — Databricks Lakehouse + Mosaic AI = AI-ready data infra. Strength: High.
- **`snowflake_customer`** — Cloud data warehouse modernization. Strength: Medium.
- **`aws_sagemaker_bedrock_customer`** — AWS Bedrock = gen-AI in production. Strength: High.
- **`azure_openai_customer`** — Azure OpenAI Service = GPT-4 in production (Ally.ai). Strength: Very High.
- **`gcp_vertex_ai_customer`** — Vertex AI / Gemini adoption. Strength: Medium.
- **`nvidia_partnership`** — NVIDIA GPU/Omniverse partnerships. Strength: Medium.
- **`cresta_observe_ai_cogito_signal`** — Agent-assist & QA on contact-center floor. Strength: Very High.
- **`five9_genesys_nice_talkdesk_customer`** — CCaaS choice predicts voice-AI readiness. Strength: High.
- **`los_lms_vendor_signal`** — Modern LOS = automation ready (defi SOLUTIONS, MeridianLink, Origence, Dealertrack, RouteOne, FIS, Black Knight, Finastra, nCino, Solifi, Alfa, TurnKey Lender). Strength: Medium.
- **`decisioning_platform_zest_pagaya`** — Zest AI, Upstart, Pagaya, Scienaptic, Provenir = ML decisioning in production. Strength: Very High.
- **`informed_iq_customer`** — Informed.IQ serves 7 of top 10 US auto lenders. Strength: Very High.
- **`point_predictive_customer`** — Fraud-detection AI; RouteOne integration. Strength: High.
- **`salient_skit_prodigal_customer`** — Direct voice-AI collections vendors deployed. Strength: Very High.
- **`voice_biometrics_or_ivr_modernization`** — Press about Nuance/Pindrop or IVR rebuild. Strength: Medium.
- **`speech_analytics_callminer_verint`** — Indicates QA/compliance data exists for fine-tuning AI. Strength: Medium.
- **`salesforce_einstein_microsoft_copilot`** — Embedded gen-AI in CRM/productivity. Strength: Medium.
- **`openai_anthropic_api_mention`** — Direct LLM API use in job postings/press/GitHub. Strength: High.
- **`langchain_huggingface_in_jobs`** — Tools mentioned in JDs = building LLM apps. Strength: High.
- **`proprietary_ai_platform_named`** — Ally.ai, Capital One Eno/Chat Concierge/Muse, Lendbuzz AIRA, Toyota IFDE. Strength: Very High.
- **`cloud_migration_press_release`** — Stellantis-Microsoft Azure 5-yr deal, etc. Strength: Medium.

### Partnership & Vendor Announcement

- **`pagaya_zest_upstart_partnership_announce`** — Public decisioning partnership = ML in origination. Strength: Very High.
- **`salient_or_voice_ai_partnership_announce`** — Direct competitor/category signal. Strength: Very High.
- **`consortium_membership`** — FSSCC, Cyber Risk Institute FS AI RMF, BPI BITS, FS-ISAC. Strength: Medium.
- **`microsoft_aws_google_strategic_alliance`** — Multi-year hyperscaler deals. Strength: High.
- **`plaid_argyle_pinwheel_truv_partnership`** — Income/employment verification API = automated underwriting. Strength: High.
- **`socure_sentilink_neuroid_partnership`** — AI fraud detection = mature risk-AI stack. Strength: High.
- **`dealertrack_routeone_integration_news`** — Auto-specific F&I infra modernization. Strength: Medium.
- **`agora_blockchain_tokenization_partnership`** — Frontier-tech partnerships (Chase + Agora/Figure for tokenized auto loans). Strength: Low.

### Strategic & Operational

- **`ai_commitment_annual_report`** — Explicit AI strategy in annual report / proxy (DEF 14A). Strength: High.
- **`digital_transformation_program_named`** — Named program (GMF "modernizing servicing and origination"). Strength: Medium.
- **`contact_center_layoffs_plus_tech_invest`** — Layoffs in ops/CC while expanding tech. Strength: Very High.
- **`cx_modernization_announce`** — CX revamp programs. Strength: Medium.
- **`generative_ai_press_mention`** — Direct "generative AI" use in official comms. Strength: Very High.
- **`ai_governance_committee`** — Named AI/ML governance committee in proxy/annual report. Strength: High.
- **`responsible_ai_framework_published`** — Public RAI policy or ethics framework. Strength: High.
- **`fs_ai_rmf_adoption_stage_signal`** — References to Treasury FS AI RMF adoption stage (Initial/Minimal/Evolving/Embedded). Strength: High.
- **`efficiency_ratio_target_disclosure`** — Public targets for cost/income ratio reductions via automation. Strength: Medium.

### Regulatory & Compliance

- **`cfpb_enforcement_action_auto`** — CFPB consent order creates urgency to modernize. Strength: High.
- **`state_regulator_action`** — Mass. Div. of Banks 2024 consent orders; CA DFPI, NY DFS. Strength: High.
- **`cfpb_complaint_volume_trending`** — Auto loan complaints volume from CFPB Consumer Complaint DB. Strength: High.
- **`gap_refund_or_repo_complaints`** — Specific CFPB hotspots voice/agentic AI addresses. Strength: High.
- **`model_risk_management_disclosure`** — SR 11-7 / SR 26-02 framework adherence. Strength: Medium.
- **`nist_ai_rmf_or_fs_ai_rmf_reference`** — Adoption of NIST framework. Strength: High.
- **`fair_lending_bias_testing_commitment`** — Public bias-testing/disparate-impact statements. Strength: Medium.
- **`udaap_collections_issue`** — UDAAP findings in collections. Strength: High.
- **`force_placed_insurance_or_servicing_action`** — July 2024 CFPB consent on force-placed insurance. Strength: Medium.
- **`tcpa_or_reg_f_lawsuit`** — TCPA/FDCPA class actions push compliant voice AI. Strength: Medium.

### Contact Center & Customer Experience

- **`contact_center_fte_count`** — Larger CC = larger AI ROI; estimate from LinkedIn / 10-K. Strength: High.
- **`cc_location_disclosure`** — Multi-site CC = cost pressure. Strength: Medium.
- **`outsourcer_relationship`** — Concentrix/Teleperformance/TTEC/Alorica/Sutherland/Genpact = candidate for AI displacement. Strength: High.
- **`trustpilot_bbb_rating_trend`** — Low ratings + "long wait times" / "couldn't reach". Strength: Medium.
- **`reddit_app_store_service_complaints`** — "Hold time"/"couldn't reach"/"GAP refund" in reviews. Strength: Medium.
- **`nps_csat_publicly_disclosed`** — J.D. Power Consumer Financing Satisfaction rank. Strength: Low.
- **`dialer_modernization_announce`** — Five9/Genesys/NICE/Talkdesk migration news. Strength: High.
- **`chatbot_named_assistant_live`** — Ally.ai, Eno, Sebastian, Erica, Fargo, Chat Concierge. Strength: High.
- **`self_service_payment_portal`** — Self-service launch = digital maturity. Strength: Medium.

### Industry Event & Marketing

- **`afsa_vehicle_finance_speaker`** — Speaking slot = thought leadership/peer pressure. Strength: High.
- **`auto_finance_summit_speaker`** — AFS Las Vegas + AFS East Nashville. Strength: High.
- **`auto_finance_excellence_award_win`** — Winners reveal AI/digital leaders. Strength: Very High.
- **`naf_non_prime_conference_speaker`** — NAF Association. Strength: Medium.
- **`fintech_breakthrough_or_ai_excellence_award`** — Lendbuzz 2025 FinTech Breakthrough Consumer Lending Innovation. Strength: Medium.
- **`published_whitepaper_or_research_on_ai`** — Co-published research with vendors/analysts. Strength: Medium.
- **`webinar_hosted_on_ai_automation`** — Hosting indicates maturity to teach. Strength: Medium.
- **`press_release_ai_initiative_count`** — Count of AI-themed press in last 12 months. Strength: High.
- **`analyst_coverage_aite_celent_forrester_gartner`** — Named in Celent/Aite/Forrester/Gartner reports on lending AI. Strength: Medium.

### Product & Business Model

- **`digital_first_auto_product`** — Online prequalification + e-contracting (Auto Navigator, Lendbuzz Express Contract). Strength: High.
- **`direct_to_consumer_refi_channel`** — Caribou, RateGenius, Tresl, AUTOPAY, Upstart auto refi. Strength: Medium.
- **`same_day_funding_capability`** — Marketing claim of same-day decision + fund. Strength: Medium.
- **`embedded_finance_partnership`** — Partnerships with OEM/dealer apps for embedded loan offers. Strength: Medium.
- **`auto_decisioning_rate_disclosed`** — Public auto-decisioning % (Toyota 60%+, Chase 80%). Strength: Very High.
- **`mobile_app_ai_features`** — In-app chatbot, smart recommendations. Strength: Medium.
- **`econtracting_adoption`** — DocuSign, eOriginal, Wolters Kluwer Vitu integration. Strength: Medium.
- **`dealer_facing_ai_copilot`** — F&I copilots (Capital One Muse, Chat Concierge). Strength: Very High.

### Collections & Servicing (Auto-specific)

- **`delinquency_rate_trend`** — Subprime 60+ DPD; rising lender-level rate. Strength: Very High.
- **`charge_off_rate_disclosure`** — 10-Q CNL/charge-off ratios. Strength: High.
- **`repo_volume_signal`** — CFPB auto-finance data pilot tracks repos; record 2.2M repos. Strength: High.
- **`voice_ai_collections_partner`** — Salient/Skit/Prodigal/Floatbot/Vodex/Layerup deployment. Strength: Very High.
- **`collections_compliance_issue`** — UDAAP, Reg F findings in collections. Strength: High.
- **`ai_call_center_kpi_disclosure`** — CACC "27% of inbound routed to AI agent". Strength: Very High.
- **`ptp_kept_rate_or_handle_time_metric`** — Disclosed % handle-time reduction. Strength: Medium.
- **`repossession_or_total_loss_workflow_ai`** — Salient total-loss agent indicates auto-specific use case maturity. Strength: High.
- **`gap_refund_automation`** — GAP refund processing is CFPB hotspot ripe for AI. Strength: Medium.
- **`title_management_automation`** — Vitu, Dealertrack title services integration. Strength: Medium.

### Data & Analytics Maturity

- **`cdo_caio_chief_data_role_exists`** — Leading indicator. Strength: High.
- **`data_lake_warehouse_modernization`** — Press about Snowflake/Databricks/Lakehouse migration. Strength: Medium.
- **`data_observability_governance_tooling`** — Acceldata, Monte Carlo, Collibra adoption. Strength: Medium.
- **`open_banking_aggregation_partnership`** — Plaid, MX, Finicity, Yodlee. Strength: High.
- **`alternative_data_underwriting`** — Cashflow underwriting, Experian Boost, Equifax Trended. Strength: High.
- **`real_time_decisioning_disclosure`** — Sub-second decisioning (Toyota IFDE). Strength: High.
- **`kelley_blue_book_or_blackbook_residual_model`** — ML-powered residual value modeling. Strength: Medium.
- **`data_science_publications_or_patents`** — Capital One 5,000+ US patents. Strength: Medium.

### Fraud & Risk

- **`socure_sentilink_neuroid_deployed`** — Identity/synthetic fraud AI. Strength: Very High.
- **`point_predictive_deployed`** — Auto-specific fraud AI; 2026 $10.4B fraud-exposure report. Strength: Very High.
- **`informed_iq_dealer_fraud_deployment`** — AI verification + GenAI-fabricated doc detection. Strength: Very High.
- **`synthetic_identity_initiative`** — Press/blog on synthetic-ID/AI-fraud. Strength: High.
- **`argyle_pinwheel_truv_voi_voe`** — Automated VOI/VOE. Strength: High.
- **`gen_ai_fabricated_doc_detection_capability`** — Mentioning detection of AI-generated stips. Strength: High.

### Earnings Call & Filing-Specific

- **`keyword_count_artificial_intelligence`** — Quarterly count in transcripts. Strength: Very High.
- **`keyword_count_generative_ai`** — Generative AI = past basic ML. Strength: Very High.
- **`keyword_count_agentic_ai`** — "Agentic" is 2025-2026 frontier vocabulary. Strength: Very High.
- **`keyword_count_voice_ai_conversational`** — Direct ICP keyword. Strength: Very High.
- **`keyword_count_automation_operational_efficiency`** — Cost-cut framing. Strength: High.
- **`keyword_count_digital_transformation`** — Often precursor to AI investment. Strength: Medium.
- **`ai_dollar_figure_disclosed`** — Specific $ allocation (BofA $3B/yr). Strength: Very High.
- **`fte_reduction_tied_to_automation`** — "X jobs replaced by AI" — strongest possible signal. Strength: Very High.
- **`ai_in_risk_factors_section`** — First-time addition of AI as risk factor (CACC 2025). Strength: Medium.
- **`ai_in_md_and_a`** — MD&A mentions = material to financials. Strength: High.

---

## Sub-Industry: Personal Loan Fintechs & Mid-Market Lenders (US)

**Universe:** Upstart, Affirm, SoFi, Pagaya, Happy Money, OppFi, Enova, OneMain, Best Egg, Achieve, Regional Management, World Acceptance, Klarna (US ops), Sezzle, LendingClub, Upgrade, Earnest, College Ave, LendingPoint, Avant, Splash Financial, Rocket.

### Hiring / Talent

- **`S-HIRE-01`** — Conversational AI / Voice AI Engineer Postings. Conf 0.9 / Weight 10. Query: `site:job-boards.greenhouse.io OR site:jobs.lever.co OR site:linkedin.com/jobs "{company}" ("conversational AI" OR "voice AI" OR "voicebot" OR "IVR" OR "speech" OR "Dialogflow" OR "Amazon Lex")`.
- **`S-HIRE-02`** — Chief AI / Head of AI / VP AI / VP Automation postings or hires. Conf 0.85 / Weight 9.
- **`S-HIRE-03`** — Head of Contact Center / Servicing Modernization roles. Conf 0.8 / Weight 9.
- **`S-HIRE-04`** — RPA / Automation Engineer / MLOps postings (UiPath, Automation Anywhere, process automation, MLOps, ML platform engineer). Conf 0.75 / Weight 7.
- **`S-HIRE-05`** — Prompt Engineer / LLM Engineer / GenAI PM roles (LangChain, RAG). Conf 0.85 / Weight 9.
- **`S-HIRE-06`** — Volume of AI/ML Job Postings YoY Growth (>25% increase). Conf 0.7 / Weight 7.

### Executive / Leadership

- **`S-EXEC-01`** — Recent Chief Data Officer / Chief Digital Officer Appointment. Conf 0.8 / Weight 8.
- **`S-EXEC-02`** — Executive Thought-Leadership on AI (LinkedIn / Earnings Calls). Conf 0.6 / Weight 7.
- **`S-EXEC-03`** — CEO Comments on AI in recent earnings transcript. Conf 0.85 / Weight 9.
- **`S-EXEC-04`** — Board / Advisory AI Expertise. Conf 0.55 / Weight 5.

### Funding / Financial

- **`S-FIN-01`** — Frequency of "AI" / "Machine Learning" in 10-K / S-1 (YoY growth ≥30%). Conf 0.85 / Weight 8.
- **`S-FIN-02`** — Operating Leverage / Cost-to-Serve Language in MD&A. Conf 0.7 / Weight 9.
- **`S-FIN-03`** — Recent IPO / Pre-IPO / Funding Round. Conf 0.65 / Weight 7.
- **`S-FIN-04`** — Stock Compensation / R&D Spend Growth Tied to AI. Conf 0.6 / Weight 6.
- **`S-FIN-05`** — Investor Day / AI Day Event (Upstart AI Day, Affirm Investor Forum). Conf 0.9 / Weight 9.
- **`S-FIN-06`** — Earnings-call mentions of "Cost-to-Serve" / "AHT" / "Contact Center Expense". Conf 0.8 / Weight 10.

### Strategic Priority

- **`S-STRAT-01`** — Public AI Strategy / Generative AI Mention in CEO Letter. Conf 0.8 / Weight 9.
- **`S-STRAT-02`** — Digital Transformation Roadmap in public filings. Conf 0.65 / Weight 7.
- **`S-STRAT-03`** — Servicing / Collections Modernization Mandate. Conf 0.75 / Weight 10. *Rationale:* Highest ABM Engine fit.
- **`S-STRAT-04`** — Underwriting AI as Core Strategy. Conf 0.95 / Weight 4. *Rationale:* Already built — signals maturity but NOT ABM Engine's wedge.
- **`S-STRAT-05`** — Member Experience / Conversational AI Product Strategy. Conf 0.85 / Weight 10.

### Product / Operational

- **`S-PROD-01`** — Public launch of AI-powered customer-facing feature. Conf 0.9 / Weight 9.
- **`S-PROD-02`** — Press release on AI partnership/integration (OpenAI, Anthropic, AWS Bedrock, Cognigy, Five9, Genesys, NICE, Talkdesk, Twilio). Conf 0.95 / Weight 10.
- **`S-PROD-03`** — Mentioned in vendor case study (zendesk.com, twilio.com, cognigy.com, five9.com, nice.com, salesforce.com). Conf 0.9 / Weight 8.
- **`S-PROD-04`** — AI Fraud Detection / KYC Launch. Conf 0.7 / Weight 6.
- **`S-PROD-05`** — Proprietary AI platform branded (Happy Money "Hive", Enova "Colossus", OppFi platform, Pagaya FastPass). Conf 0.8 / Weight 7.

### Tech Stack

- **`S-TECH-01`** — Job descriptions mention CCaaS vendor (Genesys, Five9, NICE inContact, Talkdesk, Amazon Connect, Twilio Flex, Dialogflow). Conf 0.95 / Weight 9.
- **`S-TECH-02`** — Cloud / Data Platform Vendor (Snowflake, Databricks, AWS, Azure ML, Google Cloud Vertex). Conf 0.85 / Weight 6.
- **`S-TECH-03`** — LLM Foundation Model Vendor mentioned (OpenAI, Anthropic, Bedrock, Claude, GPT-4). Conf 0.85 / Weight 9.
- **`S-TECH-04`** — BuiltWith / Wappalyzer tech stack hits (Intercom, Drift, Ada, LivePerson). Conf 0.75 / Weight 7.
- **`S-TECH-05`** — Twilio / Communications API job mentions (Twilio, Plivo, Vonage, Bandwidth). Conf 0.85 / Weight 8.

### Pain Indicators

- **`S-PAIN-01`** — CFPB Complaint Volume / Trend for Company (YoY growth >20%, "trouble during payment process" / "communication tactics"). Conf 0.85 / Weight 10.
- **`S-PAIN-02`** — Trustpilot / BBB negative themes (wait times, hard to reach, disputes unresolved, payment-posting). Conf 0.75 / Weight 9.
- **`S-PAIN-03`** — Reddit Sentiment Mining (r/personalfinance, r/CRedit, r/Debt). Conf 0.6 / Weight 7.
- **`S-PAIN-04`** — Glassdoor reviews of call-center / servicing roles (burnout, micromanagement, high volume, low pay). Conf 0.7 / Weight 8.
- **`S-PAIN-05`** — Earnings-call mentions of servicing/collections expense pressure. Conf 0.75 / Weight 9.
- **`S-PAIN-06`** — Negative app store reviews re: support. Conf 0.55 / Weight 5.

### Regulatory / Compliance

- **`S-REG-01`** — CFPB Enforcement Action. Conf 0.95 / Weight 8.
- **`S-REG-02`** — State-Level AG Action. Conf 0.85 / Weight 7.
- **`S-REG-03`** — FDCPA / TCPA / Reg F Compliance Spend. Conf 0.7 / Weight 9.
- **`S-REG-04`** — Fair Lending / ECOA Adverse Action Mandate. Conf 0.7 / Weight 7.
- **`S-REG-05`** — Compliance Officer / AI Governance Lead hire. Conf 0.8 / Weight 7.

### Volume / Scale

- **`S-VOL-01`** — Loan Origination Volume Disclosure. Conf 0.85 / Weight 8.
- **`S-VOL-02`** — Serviced Loan Portfolio Size. Conf 0.8 / Weight 8.
- **`S-VOL-03`** — Contact Center / Servicing Headcount Disclosure. Conf 0.6 / Weight 9.
- **`S-VOL-04`** — MAU / DAU / Member Count. Conf 0.8 / Weight 7.
- **`S-VOL-05`** — Number of Bank/Credit-Union Partners (for marketplace lenders). Conf 0.7 / Weight 6.

### Partnership / Vendor

- **`S-PART-01`** — Announced AI Vendor Partnership (OpenAI, Anthropic, Cognigy, Cresta, Skit, ASAPP, Replicant, Sierra AI). Conf 0.95 / Weight 10.
- **`S-PART-02`** — System Integrator Engagement (Accenture, Deloitte, EY, PwC, Genpact, Cognizant, TCS, Infosys). Conf 0.7 / Weight 7.
- **`S-PART-03`** — Fintech Infrastructure Vendor (Plaid, Method, Alloy, Persona, Socure). Conf 0.65 / Weight 5.
- **`S-PART-04`** — Collections / Recovery Vendor Switch (Sutherland, TrueAccord, Skit.ai, InDebted). Conf 0.8 / Weight 9.

### RFP / Procurement

- **`S-RFP-01`** — Public RFP for Contact Center / Conversational AI. Conf 0.9 / Weight 9.
- **`S-RFP-02`** — Government Procurement Portal mention (sam.gov, bidnet.com). Conf 0.7 / Weight 6.

### Conference / Event

- **`S-EVENT-01`** — Speaking slot at Money 20/20, Fintech Nexus, Finovate, Bank Director. Conf 0.8 / Weight 7.
- **`S-EVENT-02`** — Sponsorship of AI-in-Finance events. Conf 0.65 / Weight 5.
- **`S-EVENT-03`** — Hosted Investor "AI Day". Conf 0.95 / Weight 10.
- **`S-EVENT-04`** — Webinar / Podcast on AI in Lending. Conf 0.55 / Weight 5.

### Patent / IP

- **`S-PAT-01`** — Recent USPTO filing on ML/AI in lending. Conf 0.85 / Weight 6.
- **`S-PAT-02`** — Recent patent on conversational AI / voice in financial services. Conf 0.85 / Weight 9.

### M&A

- **`S-MA-01`** — Acquisition of AI/Data-Science Startup. Conf 0.9 / Weight 8.
- **`S-MA-02`** — Divestiture of legacy servicing / call-center operations. Conf 0.75 / Weight 8.

### Competitive Pressure

- **`S-COMP-01`** — Direct competitor publicly launched AI (Klarna for BNPL, Upstart for personal loans). Conf 0.85 / Weight 9.
- **`S-COMP-02`** — Analyst note calls out AI gap. Conf 0.6 / Weight 7.
- **`S-COMP-03`** — Press coverage of competitor's cost savings ($40M Klarna). Conf 0.7 / Weight 8.
- **`S-COMP-04`** — Loss of market share to AI-native competitor. Conf 0.55 / Weight 7.

### Cross-Cutting / Meta

- **`S-META-01`** — "AI" mentions in company tagline / hero copy (Pagaya, Upstart, OppFi). Conf 0.9 / Weight 7.
- **`S-META-02`** — AI-specific subdomain or microsite (ai.{company}.com or {company}.ai). Conf 0.85 / Weight 7.
- **`S-META-03`** — Trustpilot Verified Response Tool adoption. Conf 0.7 / Weight 5.

---

## Sub-Industry: Insurance (US)

**Universe:** Allstate, Nationwide, Travelers, USAA, Berkshire Hathaway, Liberty Mutual, American Family, AIG, Erie, CNA, Lemonade, Progressive, GEICO, Chubb, Hartford, Markel, W.R. Berkley, Zurich North America, AXA XL, Beazley, Tokio Marine, MGA platforms, UnitedHealthcare, Elevance, CVS/Aetna, Cigna, Humana, Centene, Molina, BCBS plans, Prudential, MetLife, New York Life, Northwestern Mutual, MassMutual, Lincoln Financial, Guardian, John Hancock, TPAs (Sedgwick, Crawford, Gallagher Bassett, ESIS, Helmsman, Reserv).

### Hiring (10 signals)

- **`hiring.ai_ml_role_count`** — Open AI/ML/data-science/AI engineer roles. Weight 5. Query: `site:carrier.com/careers ("machine learning" OR "ML engineer" OR "data scientist" OR "AI engineer")`. Threshold: ≥5 = strong, ≥15 = very strong.
- **`hiring.gen_ai_specialist_role`** — Generative AI / LLM / prompt engineer / MLOps / agentic AI roles. Weight 5. *Rationale:* Differentiates production gen-AI from classical ML.
- **`hiring.conversational_ai_role`** — Conversational AI / voice AI / chatbot / NLP engineer / dialog designer roles. Weight 5. *Rationale:* Direct fit for ABM Engine voice AI / CX automation.
- **`hiring.chief_ai_officer_or_equivalent`** — Chief AI Officer / Chief Data & Analytics Officer / Head of AI. Weight 5. *Rationale:* CAIO hire is a 12-month leading buy signal.
- **`hiring.contact_center_modernization_role`** — Contact center / CX transformation director/VP/head of insurance. Weight 4.
- **`hiring.platform_engineer_ccaas`** — Genesys / NICE CXone / Five9 / Talkdesk / Amazon Connect engineer. Weight 4.
- **`hiring.claims_automation_role`** — Claims automation / claims transformation / straight-through processing / FNOL automation. Weight 4.
- **`hiring.underwriting_data_science_role`** — Underwriting data scientist / predictive modeling underwriter. Weight 3.
- **`hiring.ai_governance_role`** — AI governance / model risk management / responsible AI / AI ethics insurance roles. Weight 4. *Rationale:* NAIC Model Bulletin / Colorado / NYDFS compliance work.
- **`hiring.velocity_30d`** — AI/ML req count growth >50% in last 30 days vs 90-day rolling avg. Weight 4.

### Technology Stack (8 signals)

- **`tech.core_system_modernization_active`** — Guidewire / Duck Creek / Majesco / Sapiens / EIS / Insurity modernization in last 18 months. Weight 5. *Rationale:* Single largest carrier IT spend event; AI bundled.
- **`tech.hyperscaler_partnership_announced`** — Preferred cloud / strategic cloud partnership (AWS, Azure, Google Cloud) 2024-2026. Weight 4.
- **`tech.ccaas_platform_signal`** — Genesys / NICE / Five9 / Talkdesk / Amazon Connect deployment. Weight 4.
- **`tech.data_platform_modern`** — Snowflake, Databricks, Microsoft Fabric, Confluent, dbt. Weight 4.
- **`tech.api_first_initiative`** — Developer portal / open API. Weight 3.
- **`tech.legacy_mainframe_dependency`** — Heavy legacy (COBOL/AS400) — either high friction or huge urgency for agentic modernization. Weight 3.
- **`tech.rpa_existing`** — UiPath / Automation Anywhere / Blue Prism. Weight 3. *Rationale:* Next-stage target for cognitive automation / agentic upgrade.
- **`tech.ai_vendor_already_in_house`** — Shift Technology, FRISS, Tractable, Cape Analytics, Roots AI, Indico Data, Federato. Weight 4.

### Strategic from Public Filings (6 signals)

- **`strategic.10k_ai_mentions`** — Count of "artificial intelligence" / "generative AI" / "machine learning" / "automation" in 10-K Risk Factors and MD&A. Weight 5. *Rationale:* AI in MD&A (vs only Risk Factors) signals offense.
- **`strategic.earnings_call_ai_emphasis`** — CEO/CFO language scored for AI as top-3 strategic priority. Weight 5.
- **`strategic.investor_day_ai_roadmap`** — Explicit AI savings/revenue targets with timelines (Allstate Q3 2025 — 45% billing inquiry reduction). Weight 5.
- **`strategic.digital_transformation_priority`** — Annual report / executive interview / conference keynote interpretation of "digital transformation" maturity stage. Weight 4.
- **`strategic.expense_ratio_focus`** — 10-K / earnings transcript stated cost-out initiatives. Weight 4.
- **`strategic.line_of_business_exit_announced`** — Carriers exiting CA homeowners, FL property, or unprofitable lines. Weight 3.

### Regulatory & Compliance (5 signals)

- **`reg.naic_bulletin_domicile`** — Domicile in NAIC Model Bulletin state (25+ adopters: AK, CT, DE, HI, IL, KY, MD, MA, NE, NV, NH, NJ, NC, OK, PA, RI, VT, VA, WA, WI, WV, +others). Weight 5.
- **`reg.colorado_sb21_169_obligated`** — Colorado DOI Regulation 10-1-1 compliance (life Dec 1 annually; auto + health July 1, 2026). Weight 5.
- **`reg.nydfs_circular_letter_2024_7`** — NY-authorized insurers using AIS/ECDIS in underwriting/pricing. Weight 5. *Rationale:* Mandates proxy assessment, three-step fairness test, third-party audit rights, 15-day adverse-action notice.
- **`reg.health_ai_state_restriction`** — CA SB 1120, AZ, MD, NE, TX prohibit AI-only denials in health + federal CMS MA WISeR pilot. Weight 4.
- **`reg.public_enforcement_action`** — State DOI enforcement orders, market-conduct exam findings, DOL ERISA suits. Weight 4.

### CX & Operational Pain (6 signals)

- **`cx.naic_complaint_index_high`** — NAIC Consumer Insurance Search index >1.0 (above-average complaints). Weight 5. *Rationale:* Direct measurement of dissatisfaction; index >1.5 strong signal.
- **`cx.jd_power_score_low`** — J.D. Power US Auto/Home Insurance / Digital Experience / Claims Satisfaction below industry median. Weight 4.
- **`cx.app_store_review_decline`** — iOS/Google Play carrier app rating <3.5, sentiment trending negative. Weight 3.
- **`cx.call_center_volume_pressure`** — Earnings/Glassdoor/reviews mentioning "wait times," "hold," "couldn't reach." Weight 4.
- **`cx.frontline_attrition`** — Glassdoor / layoff news / talent-shortage commentary (12-15% frontline turnover; 400K projected vacancies by 2026). Weight 4.
- **`cx.claims_cycle_time_disclosed`** — Investor decks / J.D. Power / earnings disclose cycle times (avg auto repair 22.3 days; >25 days are buyers). Weight 4.

### Partnership, Vendor & Innovation (4 signals)

- **`part.ai_vendor_partnership_announced`** — Press releases naming AI vendor (OpenAI, Anthropic, Microsoft, Google, AWS). Weight 5.
- **`part.insurtech_investment_or_acquisition`** — Active CVC arms (Allianz X, AXA Venture Partners, Munich Re Ventures, American Family Ventures, MassMutual Ventures, MS&AD Ventures, Nationwide Ventures, NYL Ventures, State Farm Ventures, Avanta Ventures, Liberty Mutual Strategic Ventures, Prudential Capital). Weight 4.
- **`part.innovation_lab_or_accelerator`** — USAA Innovation Lab, Hartford IoT Lab, Travelers Innovation, Liberty Mutual Solaria Labs, AIG Atlanta agentic AI lab, Nationwide AI center. Weight 4.
- **`part.consulting_partner_engagement`** — Big-4 / SI press: Accenture, Deloitte, EY, PwC, Cognizant, TCS, Infosys, Wipro. Weight 3.

### Financial (4 signals)

- **`fin.combined_ratio_pressure`** — S&P GMI, AM Best, Fitch reports; personal-lines mutuals at 107.9 cumulative CR 2021-2023; commercial auto 107.2 in 2024; "other liability" 110.1. Weight 4.
- **`fin.loss_adjustment_expense_trend`** — LAE growth without claim-count growth = inefficiency. Weight 4.
- **`fin.expense_ratio_above_peer`** — NAIC filings vs peer group. Weight 3.
- **`fin.am_best_outlook_negative`** — AM Best outlook revisions. Weight 3.

### Market & Competitive (3 signals)

- **`mkt.competitor_ai_pressure`** — Carrier's AI public footprint vs top-3 in-state/in-line competitors. Weight 3.
- **`mkt.shopping_rate_high_in_segment`** — J.D. Power shopping rate data (home shopping rate 6.8% Q2 2024). Weight 3.

### Claims & Underwriting-Specific (3 signals)

- **`claims.fnol_digital_disclosed`** — Press / investor decks identifying FNOL as digital/automated, partial, or phone-only. Weight 4.
- **`uw.alternative_data_disclosed`** — NYDFS filings, NAIC AI/ML surveys; earnings/10-K mentions of ECDIS, telematics, satellite imagery, IoT, social/digital data. Weight 4.

---

## Sub-Industry: Collections & Recovery (US)

**Universe:** Encore Capital Group / Midland Credit Management, PRA Group / Portfolio Recovery Associates, Sherman Financial / LVNV Funding / Resurgent, Transworld Systems (TSI), Alorica, IC System, GC Services (InteLogix), Performant Recovery, Receivables Performance Management, Convergent Outsourcing, Jefferson Capital, Caine & Weiner, Altus Receivables Management, The Kaplan Group, Atradius Collections, Coface, ABC-Amega, MOHELA, Nelnet, Aidvantage (Maximus), Edfinancial, R1 RCM, Ensemble Health Partners, Conifer, FinThrive, Waystar, AKASA, Tratta.

### Hiring (10 signals)

- **`H-01`** — Conversational/Voice AI role in collections. Conf 5. Query: `("conversational AI" OR "voice AI" OR "voicebot") AND (collections OR "accounts receivable" OR "ARM" OR recovery)`. *Rationale:* Strongest direct signal of internal AI buying program.
- **`H-02`** — Automation/RPA role in collections ops (UiPath, Automation Anywhere). Conf 4.
- **`H-03`** — VP/Director/Chief of Digital, Innovation, or Transformation (collections-adjacent), <12 mo tenure. Conf 5. *Rationale:* New digital execs run 90-day "modernize stack" reviews.
- **`H-04`** — Contact center hiring surge (25+ "collector" / "recovery agent" reqs open simultaneously). Conf 4.
- **`H-05`** — Hiring freeze or layoffs paired with AI/digital pitch (headcount flat while volume rises — Encore: "collections rose 20% while headcount flat for three consecutive years"). Conf 5.
- **`H-06`** — Strategy/Innovation roles in collections ("Strategy Manager – Collections," "Innovation Lead – ARM"). Conf 3.
- **`H-07`** — Quality / Compliance Analytics roles citing AI (Observe, CallMiner, Verint, NICE, Sedric). Conf 3.
- **`H-08`** — Offshore/nearshore collections expansion (Manila, Bogotá, Mexico City, Costa Rica, India new site openings). Conf 3.
- **`H-09`** — Collector attrition >40% (Glassdoor burnout reviews; financial-services contact center turnover 47-61%). Conf 4.
- **`H-10`** — Onshore/nearshore re-shoring announcements ("Keep Call Centers in America Act" S.2495). Conf 3.

### Technology & Vendor Stack (13 signals)

- **`T-01`** — Uses LiveVox, TCN, Noble, DialConnection, Ontario Systems, Intelligent Contacts, Convoso, Five9, Genesys (Latitude), NICE CXone. Conf 4.
- **`T-02`** — Still on on-prem dialer / legacy ACD (Aspect, Avaya CMS, mainframe, COBOL, AS/400). Conf 2. *Rationale:* Warm-incumbent-displacement play.
- **`T-03`** — Migration to cloud contact center (Genesys Cloud, NICE CXone, Five9, Amazon Connect). Conf 5.
- **`T-04`** — Existing speech analytics deployment (CallMiner, Verint, NICE Nexidia, Observe.AI, Prodigal). Conf 5.
- **`T-05`** — Reg F / TCPA compliance tech (NICE NEVA, Gryphon, Sedric, TCN Natural Language Compliance). Conf 4.
- **`T-06`** — RPA platforms in use (UiPath, Automation Anywhere, Blue Prism). Conf 3.
- **`T-07`** — Salesforce Financial Services Cloud / custom CRM for collections. Conf 3.
- **`T-08`** — Consumer self-service portal in production (TrueAccord/Tratta/Intelligent Contacts pattern). Conf 4.
- **`T-09`** — Active SMS/email collections, Reg F compliant (Sinch, Twilio, Solutions by Text). Conf 3.
- **`T-10`** — Public AI vendor partnership in collections (Skit.ai, Prodigal, Sedric, Cresta, Floatbot, Vodex, Aktos, Moveo, Observe.AI). Conf 5.
- **`T-11`** — Mention of "agentic AI" or "generative AI" in product/marketing copy. Conf 4.
- **`T-12`** — Native developer API / public documentation. Conf 3.
- **`T-13`** — Mention of skip tracing / data enrichment partners (LexisNexis Risk, TLO, Experian, BTRS). Conf 2.

### Regulatory & Compliance (11 signals)

- **`R-01`** — Active CFPB enforcement action / consent order (<3 yr). Conf 5.
- **`R-02`** — High CFPB Complaint Database volume (>250 complaints/year or >2x peer median). Conf 5.
- **`R-03`** — Named in active TCPA class action (2024-2026). Conf 5. *Rationale:* Compliant AI voice agents reduce TCPA exposure.
- **`R-04`** — Named in active FDCPA / Reg F lawsuit. Conf 3.
- **`R-05`** — State AG enforcement action. Conf 4.
- **`R-06`** — FTC enforcement (2025 trend: 6 of 9 actions led by FTC). Conf 4.
- **`R-07`** — CFPB Supervisory Highlights mentions (student loan collectors, medical debt). Conf 3.
- **`R-08`** — State medical-debt credit-reporting laws (CO, NY, +7 states in 2024). Conf 3.
- **`R-09`** — TCPA consent infrastructure investments (consent management, DNC scrubbing, Gryphon, ActiveProspect). Conf 4. *Rationale:* Required predicate for AI-voice after FCC Feb 2024 ruling.
- **`R-10`** — NMLS / state license activity / surety bond size (recent license additions). Conf 2.
- **`R-11`** — PCI DSS, SOC 2, HITRUST certification announcements. Conf 2.

### Strategic & Executive (9 signals)

- **`S-01`** — Earnings call mentions AI / automation / digital transformation in collections (Encore Q1 2026 "another level of technology"). Conf 5.
- **`S-02`** — 10-K / 10-Q Risk Factors cite legacy tech or compliance cost. Conf 4.
- **`S-03`** — Executive thought leadership posts on AI in collections (LinkedIn, Receivables Info, ACA International podcasts). Conf 4.
- **`S-04`** — Published case study with AI vendor (Skit.ai 53,000+ creditors; Prodigal, Cresta, Sedric, Floatbot publish lists). Conf 5.
- **`S-05`** — Board addition with tech/AI background (proxy / 8-K appointments). Conf 3.
- **`S-06`** — Investor presentation slide on "Digital Strategy" or "Cost-to-Collect" (Encore IR: "over 50% of new payments take place digitally"). Conf 4.
- **`S-07`** — Mentions of "right-party contact" pressure or "RPC declining" (industry avg RPC ~26%). Conf 4.
- **`S-08`** — Strategic plan filed for "cost-to-collect reduction" (McKinsey: 30-60% cost-to-collect reduction with AI in RCM). Conf 4.
- **`S-09`** — "Empathy-first" or "consumer-centric" repositioning (Sedric/Floatbot LEXI marketing). Conf 3.

### Volume & Operational (10 signals)

- **`V-01`** — Rising portfolio placements / debt purchases (Encore +26% YoY 2024; PRA cash collections $1.9B 2024). Conf 4.
- **`V-02`** — Charge-off / delinquency exposure rising (credit card charge-offs 10-year highs Q1 2025). Conf 4.
- **`V-03`** — Disclosed RPC, AHT, or "cost-per-collection" KPI. Conf 4.
- **`V-04`** — Call center / FTE seat count >500 (LinkedIn + state employment filings). Conf 3.
- **`V-05`** — Disclosed >25% YoY revenue growth in ARM segment. Conf 4.
- **`V-06`** — Disclosed margin compression (TransUnion 2025: 48% of agencies cite agent productivity/margin as PRIMARY AI motivator). Conf 5.
- **`V-07`** — Site closure / consolidation (WARN Act filings). Conf 3.
- **`V-08`** — Student loan default cliff exposure (PSC list, ED contracts; 5.3M borrowers in default post-May 2025). Conf 5.
- **`V-09`** — Healthcare A/R days increase (HFMA MAP Award filings; 80% of health systems on AI in RCM). Conf 4.
- **`V-10`** — BNPL/fintech lender with growing collections org (>30% headcount growth YoY). Conf 4.

### CX Pain & Reputation (8 signals)

- **`C-01`** — High CFPB complaint count per $M revenue (45% of 2024 complaints were "debt not owed"). Conf 5.
- **`C-02`** — BBB rating below B+ / >100 complaints in 3 years (PRA, Midland 1,000+ BBB complaints). Conf 3.
- **`C-03`** — Trustpilot / Google Reviews on hold times, harassment, voicemail spam. Conf 3.
- **`C-04`** — Reddit r/personalfinance / r/CRedit threads about company. Conf 2.
- **`C-05`** — Consumer-facing app with low ratings (<3.5 stars or >1,000 negative reviews). Conf 3.
- **`C-06`** — Public apology / remediation press release ("improving customer experience" commitments). Conf 4.
- **`C-07`** — State AG complaint volume. Conf 3.
- **`C-08`** — Voicemail bombing / spam-likely flagged (First Orion, Hiya, Truecaller; YouMail Robocall Index). Conf 4.

### Financial & M&A (9 signals)

- **`F-01`** — Recent PE investment in ARM/RCM firm <24 months (PE-backed strategic buyers 36% of 1H 2024 ARM deals). Conf 5.
- **`F-02`** — Bolt-on acquisition by ARM platform (Vereda, Hilco Receivables, Resurgent). Conf 4.
- **`F-03`** — Public ARM company under activist / earnings pressure. Conf 3.
- **`F-04`** — Funding round announcement for collections fintech (Series A+ in last 12 mo). Conf 4.
- **`F-05`** — 10-K mentions "technology investments" line item growing. Conf 3.
- **`F-06`** — IPO filing or S-1 mentioning AI/automation (Jefferson Capital 2025 IPO). Conf 4.
- **`F-07`** — Revenue contraction announced. Conf 3.
- **`F-08`** — Goodwill impairment / restructuring charge. Conf 2.
- **`F-09`** — Bond / credit facility refinancing with growth language. Conf 2.

### Industry Event & Association (8 signals)

- **`E-01`** — Exhibits/speaks at RMAi Annual Conference (2025: 1,100+ ARM pros, "Technology: AI and Digital Communications" track). Conf 4.
- **`E-02`** — Exhibits/speaks at ACA International Convention / Fall Forum (multiple AI-track sessions 2025). Conf 4.
- **`E-03`** — Speaker at HFMA Annual or Revenue Cycle Conference. Conf 4.
- **`E-04`** — AFSA Vehicle Finance Conference attendance. Conf 3.
- **`E-05`** — NCBA (creditors bar) or NEDCE attendance. Conf 2.
- **`E-06`** — Auto Finance Summit speaker on chatbots/AI ("Deploying chatbots to improve collections" session). Conf 5.
- **`E-07`** — Innovation award nomination (Auto Finance Excellence, KLAS, Black Book). Conf 3.
- **`E-08`** — ACA "Visionaries" or RMAi Executive Summit invitee. Conf 4.

### Competitive & Market (5 signals)

- **`K-01`** — Direct competitor announces AI-voice deployment (named competitor goes live with Skit/Vodex/Floatbot/Prodigal/Cresta). Conf 5.
- **`K-02`** — TransUnion / FICO / Fair Isaac mentions company in analyst report. Conf 3.
- **`K-03`** — Partnership announcement with neobank or fintech lender. Conf 3.
- **`K-04`** — Public benchmark publication (recovery rate, RPC, AHT). Conf 3.
- **`K-05`** — Industry consolidation press (3rd-party agency count declined from 10,550 in 2012 to 6,908 in 2022). Conf 2.

### Digital Maturity (9 signals)

- **`D-01`** — Modern web stack (React, Next.js, Cloudflare, headless CMS) via BuiltWith/Wappalyzer. Conf 2.
- **`D-02`** — Mobile-first consumer portal (responsive, low-friction UX). Conf 3.
- **`D-03`** — Multi-payment options (ACH, debit, digital wallet, BNPL settlement). Conf 3.
- **`D-04`** — SMS / email / chat / voice all available (TransUnion 2024: email/SMS engagement +9% YoY). Conf 3.
- **`D-05`** — Twilio, Sinch, Vonage, Solutions by Text used (DNS/MX records, BuiltWith). Conf 2.
- **`D-06`** — Single sign-on / federated identity. Conf 2.
- **`D-07`** — Public API documentation or developer portal. Conf 3.
- **`D-08`** — Has an AI / chatbot already on website (manual visit, widget signature scan). Conf 4.
- **`D-09`** — Published Privacy Notice covers "automated decisioning". Conf 3.

---

## Document Summary

**Industries covered:** 2 (Retail, Financial Services)
**Sub-industries covered:** 11
**Total signals:** ~500+ (all classified as deterministic)

**Retail (7 sub-industries):**
1. Auto Parts Retail — 30 signals
2. E-commerce & D2C — 62 signals
3. Grocery & Food Retail — ~60 signals
4. Home & Furniture Retail — 54 signals
5. Beauty & Personal Care — ~110 signals
6. Apparel & Fashion — 48 signals
7. Consumer Electronics — 52 signals

**Financial Services (4 sub-industries):**
1. Auto Loans & Auto Financing — 80+ signals
2. Personal Loan Fintechs & Mid-Market Lenders — 35+ signals
3. Insurance — 47 signals
4. Collections & Recovery — ~60 signals

