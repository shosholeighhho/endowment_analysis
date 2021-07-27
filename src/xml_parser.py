import os
import pandas as pd
import xml.etree.ElementTree as ET


part_5_1_groups = ['CYEndwmtFundGrp', 'CYMinus1YrEndwmtFundGrp', 'CYMinus2YrEndwmtFundGrp', 'CYMinus3YrEndwmtFundGrp', 'CYMinus4YrEndwmtFundGrp']
part_5_1_subgroups = ['BeginningYearBalanceAmt', 'ContributionsAmt', 'InvestmentEarningsOrLossesAmt', 'GrantsOrScholarshipsAmt', 'OtherExpendituresAmt']
part_5_additional_groups = ['BoardDesignatedBalanceEOYPct','PrmnntEndowmentBalanceEOYPct','TermEndowmentBalanceEOYPct','EndowmentsHeldUnrelatedOrgInd','EndowmentsHeldRelatedOrgInd','RelatedOrgListSchRInd']

part_7_groups = ['FinancialDerivativesGrp','CloselyHeldEquityInterestsGrp','OtherSecuritiesGrp']
part_7_subgroups = ['BookValueAmt','MethodValuationCd','Desc']
part_7_additional_groups = ['TotalBookValueSecuritiesAmt']


data = []
for filename in os.listdir("../data")[:500]:

	tree = ET.parse(f'../data/{filename}')
	root = tree.getroot()
	ein = root.find('.//{http://www.irs.gov/efile}EIN').text

	answers = {}

	for group in part_5_1_groups:

		cy_group = root.find('.//{http://www.irs.gov/efile}' + group)
		if cy_group:
			for i, subgroup in enumerate(part_5_1_subgroups):
				answer = cy_group.find('.//{http://www.irs.gov/efile}' + subgroup)
				if answer is not None:
					answers[group + '_' + subgroup] = answer.text


	for group in part_5_additional_groups:
		response = root.find('.//{http://www.irs.gov/efile}' + group)
		if  response is not None:
			answers[group] = response


	for group in part_7_groups:

		cy_group = root.find('.//{http://www.irs.gov/efile}' + group)
		if cy_group:
			for i, subgroup in enumerate(part_7_subgroups):
				answer = cy_group.find('.//{http://www.irs.gov/efile}' + subgroup)
				if  answer is not None:
					answers[group + '_' + subgroup] = answer.text


	for group in part_7_additional_groups:
		response = root.find('.//{http://www.irs.gov/efile}' + group)
		if  response is not None:
			answers[group] = response

	if len(answers) > 0:
		data.append(answers)

df = pd.DataFrame(data)
df.to_csv('test.csv', index=False)







